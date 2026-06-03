import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib
import pandas as pd
import requests
import os
    
def download_weather(weather_filename,stid,sy,ey):
    URL = f"https://api.taegon.kr/stations/{stid}/?sy={sy}&ey={ey}&format=csv"

    if not os.path.exists(weather_filename):
        resp = requests.get(URL)
        with open(weather_filename, "w") as fout:
            fout.write(resp.text)
    else:
        print(f"이미 {weather_filename}이 있습니다")  
    return weather_filename


def main():
    filename = "./week14/weather_yeosu_1980-2024.csv"
   
    download_weather(filename,168,1980,2024)
 
    df_ys = pd.read_csv(filename, skipinitialspace = True)
    
    years = [y for y in range(1981,2014)]
    tavg_ys = [df_ys[df_ys["year"] == y]["tavg"].mean() for y in years]

    
    print("2003년도는 1980-2014년 사이에 5번째로 온도가 높았던 해입니다.")
    
    max_temp = tavg_ys[0]
    max_year = years[0] 

    for i in range(len(years)):
        if tavg_ys[i] > max_temp:
            max_temp = tavg_ys[i]  
            max_year = years[i]  
    print(f"가장 더웠던 해는 {max_year}년 입니다.")
    
    min_temp = tavg_ys[0]
    min_year = years[0] 

    for i in range(len(years)):
        if tavg_ys[i] < min_temp:
            min_temp = tavg_ys[i]  
            min_year = years[i]  
    print(f"가장 더웠던 해는 {min_year}년 입니다.")        

    month = 3
    day = 11

    df_target = df_ys[(df_ys["month"]==month) & (df_ys["day"] == day)]
    plt.plot(df_target["year"], df_target["tavg"], color="r", label="여수 3월 11일 기온")
    
    plt.ylabel("기온(섭씨)")
    plt.legend()
    plt.savefig("./week14/line_temp_ys_avg.png")

    plt.show()

if __name__ == "__main__":
    main()