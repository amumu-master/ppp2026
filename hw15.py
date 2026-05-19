import requests
import os
def read_weather_col(weather_filename, num, conv=float):
    dataset=[]
    with open(weather_filename)as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv(tokens[num]))
    return dataset

def weather_data_download(year=2023):
    URL = f"https://api.taegon.kr/stations/146/?sy={year}&ey={year}&format=csv"

    filename = f"week12/weather_{year}.csv"

    if not os.path.exists(filename):
        resp = requests.get(URL)
        with open(filename, "w") as fout:
            fout.write(resp.text)
    else:
        print(f"이미 {filename}이 있습니다")  
    return filename
    
def over_500mm(rainfall):
    datasets= []
    for i in rainfall:
        if i >= 5:
            datasets.append(i)
    return datasets
       
def main():
    year = 2023
    weather_filename = weather_data_download(year)
    rainfall = read_weather_col(weather_filename, 9)
    tavg = read_weather_col(weather_filename,4)
    rain500 = over_500mm(rainfall)
    print(f"{year}년도의 연 평균 기온은 {round(sum(tavg)/len(tavg))}도 입니다.")
    print(f"{year}년도 5mm이상 강우일수는 {len(rain500)}일 입니다")
    print(f"{year}년도 총 강우량은 {round(sum(rainfall),1)}mm 입니다.")
  

if __name__=="__main__":
    main()