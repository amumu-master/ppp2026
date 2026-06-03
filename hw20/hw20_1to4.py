import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import requests

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
    filename = "./week14/weather_jeonju_1980-2024.csv"
    filename_s = "./week14/weather_suwon_1980-2024.csv"

    download_weather(filename,146,1980,2024)
    download_weather(filename_s,119,1980,2024)
 
    df_sw = pd.read_csv(filename_s, skipinitialspace = True)
    df = pd.read_csv(filename, skipinitialspace=True)
    x = 2012
    y = 2024
    z = 2020
    xx = 2019
    df["tdif"] = df["tmax"] -df["tmin"]
    prec_jj =  df[df["year"] == xx]["rainfall"].sum()
    prec_sw = df_sw[df_sw["year"] == xx]["rainfall"].sum()

    print(f"전주시 {x}년 연 강수량은 {df[df["year"] == x]["rainfall"].sum():.1f}mm 입니다.")
    print(f"전주시의 {y}년 쵀대기온은 {df[df["year"] == y]["tmax"].max()}도 입니다.")
    print(f"전주시의 {z}년 최대 일교차는 {df[df["year"] == 2024]["tdif"].max()}도 입니다.")
    print(f"수원시와 전주시의 2019년 총강수량 차이는 {abs(prec_jj - prec_sw):.1f}(절댓값)mm 입니다.")

    for year in range(1981,2024):
        tavg_jj = df[df["year"] == year]["tavg"].mean()

if __name__=="__main__":
    main()