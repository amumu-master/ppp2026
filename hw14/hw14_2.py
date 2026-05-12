def read_weather_col(weather_filename, num):
    values=[]
    with open(weather_filename)as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[num])
            values.append(value)
    return values

def read_dates(weather_filename):
    dates = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            date = [int(tokens[0]), int(tokens[1]), int(tokens[2])]
            dates.append(date)
    return dates

def gdd_season(dates, tavg):
    datasets = []
    for year in range(2001,2023):
        gdd_value = 0
        for i in range(len(dates)):
            if dates[i][0] == year:
                date = dates[i]
                t = tavg[i]
                if date[1] in [5,6,7,8,9]:  
                    if t >= 5:      
                            gdd_value += (t - 5)
        datasets.append([year, gdd_value])               
    return datasets

def main():
    weather_filename = "week10/weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tavg = read_weather_col(weather_filename, 4)
    gdd_values = gdd_season(dates, tavg)
    
    for i in range(len(gdd_values)):
        print(f"{gdd_values[i][0]}년도의 5월부터 9월까지의 적산온도는 {round(gdd_values[i][1] ,1)}도 입니다.")

if __name__=="__main__":
    main()