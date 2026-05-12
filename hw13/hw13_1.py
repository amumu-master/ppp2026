def read_weather_col(weather_filename, num=9, conv=float):
    dataset=[]
    with open(weather_filename)as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv(tokens[num]))
    return dataset  

def sumifs(rainfalls, months, selected_month = [6,7,8]):
    total_value = 0
    for i in range(len(rainfalls)):   
        r = rainfalls[i]
        m = months[i]
        if m in selected_month: 
            total_value +=r
    return total_value
    

def main():
    weather_filename = "week09/weather(146)_2022-2022.csv"
    rainfall=read_weather_col(weather_filename)
    months = read_weather_col(weather_filename, 1, int)
    summer_rainfall = sumifs(rainfall, months)
    print(f"2022년도의 여름철 강수량은 {summer_rainfall:.1f}mm 입니다.")

if __name__=="__main__":
    main()