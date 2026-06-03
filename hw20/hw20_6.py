import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import requests
import koreanize_matplotlib

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
    download_weather(filename,146,1980,2024)
 
    df = pd.read_csv(filename, skipinitialspace=True)
    
    fig, ax = plt.subplots(figsize=(15, 6))
    year = [x+1980 for x in range(45)]
    rain = [df[df["year"] == y]["rainfall"].sum() for y in year]
    ax.bar(year, rain, color="b")
    ax.set_ylabel("연간 총강우량(mm)")
    fig.savefig("./week14/bar_rain_jj.png")  
    plt.show()
   
if __name__=="__main__":
    main()