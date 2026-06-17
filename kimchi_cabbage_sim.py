import PySimpleGUI as sg
import os
from datetime import date
import asyncio
import telegram
import requests


def weather_data_download():
    URL = f"https://api.taegon.kr/stations/146/?sy=1980&ey=2024&format=csv"

    filename = "kimchi_cabbage_farm/weather_jeonju_1980-2024.csv"

    if not os.path.exists(filename):
        resp = requests.get(URL)
        with open(filename, "w") as fout:
            fout.write(resp.text)
    else:
        None
    return filename
 
def read_day_weather(filename,month,day):
    tavg_list=[]
    tmax_list=[]
    tmin_list=[]
    rainfall_list=[]
    hum_list=[]
    
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            y = int(tokens[0])
            m = int(tokens[1])
            d = int(tokens[2])
            if m == month and d == day:
                tavg_list.append(float(tokens[4]))
                tmax_list.append(float(tokens[3]))
                tmin_list.append(float(tokens[5]))
                hum_list.append(float(tokens[6]))
                rainfall_list.append(float(tokens[9]))
 
    return {"tavg" : round(sum(tavg_list)/len(tavg_list)), "tmax":round(sum(tmax_list)/len(tmax_list)),"tmin":round(sum(tmin_list)/len(tmin_list)),"hum":round(sum(hum_list)/len(hum_list)),"rainfall":round(sum(rainfall_list)/len(rainfall_list))}
 
def gdd_cal(tmin,tmax,gdd):
    gdd_today = (tmax +tmin)/2 -5
    if gdd_today < 0:
        gdd_today = 0
    gdd += gdd_today
    return round(gdd, 1)
 
def cabbage_stage(gdd):                                     # GDD 계산 기준 (Tb=5°C, 수확 적기 750~870)
                                                             # 출처: Sim et al. (2021), Horticultural Science and Technology                                                       # DOI: https://doi.org/10.7235/HORT.20210063
    if gdd <= 100:
        return "파종기"   #발아-정식 준비 기간
    if gdd <= 300:
        return "유묘기"   #정식후 4-6주
    if gdd <= 550:
        return "생장기"   #잎 생장 급증 구간
    if gdd <= 750:
        return "결구기"   #결구기
    if gdd >  750:
        return "수확기"   # 750-870 
    
def events_weather(t_w, cold_days, dry_days,gdd):
    weather_events = []
    
    if t_w["rainfall"] ==0 and t_w["hum"] < 50:
        dry_days+=1
    else:
        dry_days=0
    if t_w["tavg"] <= 13:
        cold_days += 1
    else:
        cold_days=0
 
    if t_w["tavg"] >= 30:
        weather_events.append("고온")     # 차광망, 관수 필요
    if t_w["rainfall"] >= 80:
        weather_events.append("호우")     # 배수로 정비
    if dry_days >= 5:
        weather_events.append("가뭄")     # 관수 필요
    if t_w["tavg"] <= -6 :
        weather_events.append("한파")     # 한랭사 필요
    if cold_days >= 7 and gdd >= 100 :     #나중에 콜드대이스 하나씩 더할때  gdd 기준값도 줘야 할듯
        weather_events.append("추대")   
    
    return weather_events, cold_days, dry_days
 
def events_pest(weather_events,t_w,stage):    #무름병 진딧물 뿌리혹병
    pest_events = []
    
    if stage != "파종기":
        if 30 <= t_w["tavg"] and ("호우" in weather_events or t_w["hum"]>=80):
            pest_events.append("무름병")
        if t_w["tavg"] >= 20 and t_w["hum"] <=60 and t_w["rainfall"] == 0:
            pest_events.append("진딧물")
        if  15<= t_w["tavg"] <= 25 and t_w["hum"]>=80:
            pest_events.append("뿌리혹병")
 
    return pest_events
 
    
def save_state(state):
    with open("kimchi_cabbage_farm/save.txt", "w") as f:
        for k, v in state.items():
            f.write(f"{k}={v}\n")
 
def load_state():
    if not os.path.exists("kimchi_cabbage_farm/save.txt"):
        return None
    state = {}
    with open("kimchi_cabbage_farm/save.txt") as f:
        for line in f:
            k, v = line.strip().split("=", 1)
            state[k] = v
    return state
 
def cabbage_health(pest_events, weather_events, health, use_items):
    if "호우" in weather_events and "배수로 정비" not in use_items:
        health -= 3
    if "한파" in weather_events and "한랭사" not in use_items:
        health -= 4
    if "고온" in weather_events and "차광망" not in use_items:
        health -= 2
    if "가뭄" in weather_events and "관수" not in use_items:
        health -= 2
 
    if "무름병" in pest_events and "살균제" not in use_items:
        health -= 5
    if "진딧물" in pest_events and "살충제" not in use_items:
        health -= 3
    if "뿌리혹병" in pest_events and "석회처리" not in use_items:    #토양 산성 방지
        health -= 4
 
    if "추대" in weather_events:
        health = 0
 
    if health < 0:
        health = 0
    return health
 
def health_s(health):
    if health <= 0:    
        health_stage = "고사"
    elif health <= 10: 
        health_stage = "비상"
    elif health <= 30: 
        health_stage = "위험"
    elif health <= 60: 
        health_stage = "악화중"
    else:              
        health_stage = "정상"
    return health_stage
 
    
def main():
    weather_data_download()
    filename = "kimchi_cabbage_farm/weather_jeonju_1980-2024.csv"
 
    save = load_state()
    if save:
        ans = sg.popup_yes_no("저장된 게임이 있어요. 이어할까요?")
        if ans == "Yes":
            gdd       = float(save["gdd"])
            health    = float(save["health"])
            coins     = int(save["coins"])+1
            cold_days = int(save["cold_days"])
            dry_days  = int(save["dry_days"])
            if save["last_date"] == str(date.today()):
                coins = int(save["coins"])       # 같은 날이면 그대로
            else:
                coins = int(save["coins"]) + 1
        else:
            gdd = 0; health = 200; coins = 3
            cold_days = 0; dry_days = 0
    else:
        gdd = 0; health = 200; coins = 3
        cold_days = 0; dry_days = 0
 
    while True:
        today = date.today()
        t_w = read_day_weather(filename,today.month,today.day)
        use_items = []
 
        gdd = gdd_cal(t_w["tmin"],t_w["tmax"],gdd)
        stage = cabbage_stage(gdd)
        weather_events, cold_days, dry_days = events_weather(t_w,cold_days,dry_days,gdd)
        pest_events = events_pest(weather_events,t_w,stage)
        health_stage = health_s(health)
 
        layout = [
            [sg.Text("배추 키우기")],
            [sg.Text(f"{today.month}월 {today.day}일 ㅣ 기온: {t_w['tavg']}°C  습도: {t_w['hum']}% 강수량:{t_w['rainfall']}mm")],
            [sg.Text("ㅡ"*50)],
            [sg.Text(f"GDD: {gdd} ({stage})")],
            [sg.Text(f"건강도: {health} ({health_stage})")],
            [sg.Text(f"코인: {coins}", key="-COINS-")],
            [sg.Text("ㅡ"*50)],
            [sg.Text(f"[ 병충해 ] : {pest_events}")],
            [sg.Text(f"[ 기상 이벤트 ] : {weather_events}")],
            [sg.Text("ㅡ"*50)],
            [sg.Text("[ 아이템 사용 ]")],
            [sg.Button("관수"), sg.Button("살균제"), sg.Button("살충제"),sg.Button("차광망")],
            [sg.Button("석회처리"),sg.Button("배수로 정비"), sg.Button("한랭사")],
            [sg.Text("ㅡ"*50)],
            [sg.Button("오늘 완료", size=(15, 1))]            
            ]
 
        window = sg.Window("Kimchi Cabbage Farming Simulator", layout, size=(400,450))
 
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "오늘 완료"):
                break
 
            item_list = ["관수", "살균제", "살충제", "차광망", "석회처리","배수로 정비","한랭사"]
            if event in item_list:
                if coins <= 0:
                    sg.popup("코인이 없습니다!")
                else:
                    if event not in use_items:
                        coins -= 1
                        window["-COINS-"].update(f"코인: {coins}")
                        use_items.append(event)
                        sg.popup(f"{event} 사용 완료!")
                    else:
                        sg.popup(f"{event}는 이미 사용했어요!")
 
        window.close()
 
        health = cabbage_health(pest_events, weather_events, health, use_items)
 
        
        
        if "추대" in weather_events:
            sg.popup("추대가 발생했습니다. 꽃 핀 배추가 되었어요.", title="게임 오버")
            break
 
        if health <= 0:
            sg.popup("배추가 죽었습니다. 게임 오버.", title="게임 오버")
            break
        
        if gdd >= 750:
            if gdd > 870:
                result = "수확이 늦은 배추"
            elif health <= 10:
                result = "병든 배추"
            elif health <= 30:
                result = "왜소한 배추"
            elif health <= 60:
                result = "평범한 배추"
            else:
                result = "맛있는 배추"
            sg.popup(f"수확! → {result}", title="수확!")
            break
        
        if save and save.get("last_date") == str(date.today()):
                pass
        else:
            coins += 1
        save_state({
            "gdd" : gdd, "health": health, "coins" : coins, "cold_days": cold_days,"dry_days" : dry_days, "last_date": str(date.today())})
 
        sg.popup("오늘 완료! 내일 다시 실행하세요.", title="저장 완료")
        break
 
 
if __name__ == "__main__":
    main()
 