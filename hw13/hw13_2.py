def read_weather_col(weather_filename, num=9, conv=float):
    dataset=[]
    with open(weather_filename)as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv(tokens[num]))
    return dataset  

def sumifs(rainfalls, years, selected_year):
    total_value = 0
    for i in range(len(rainfalls)):   
        r = rainfalls[i]
        m = years[i]
        if m in selected_year: 
            total_value +=r
    return total_value
    
def main():
    weather_filename = "week10/weather(146)_2001-2022.csv"
    rainfall=read_weather_col(weather_filename)
    years = read_weather_col(weather_filename, 0, int)
    rainfall_2021 = sumifs(rainfall, years, [2021])
    rainfall_2022 = sumifs(rainfall, years, [2022])

    print(f"2021년 강수량은 {rainfall_2021:.1f}mm 입니다.")
    print(f"2022년 강수량은 {rainfall_2022:.1f}mm 입니다.")
    
if __name__=="__main__":
    main()