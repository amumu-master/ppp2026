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
    filename = "./week14/weather_jeonju_1980-2024.csv"
    filename_s = "./week14/weather_suwon_1980-2024.csv"
    
    download_weather(filename,146,1980,2024)
    download_weather(filename_s,119,1980,2024)
 
    df_sw = pd.read_csv(filename_s, skipinitialspace = True)
    df = pd.read_csv(filename, skipinitialspace=True)
    
    year = [x+1980 for x in range(45)]
    tavg_sw = [df_sw[df_sw["year"] == y]["tavg"].mean() for y in year]
    tavg_jj = [df[df["year"] == y]["tavg"].mean() for y in year]
    plt.plot(year, tavg_jj, color="r", label="전주")
    plt.plot(year, tavg_sw, color="b", label="수원")
    
    plt.ylabel("기온(섭씨)")
    plt.legend()
    plt.savefig("./week14/line_temp_avg.png")

  
    plt.show()

if __name__ == "__main__":
    main()