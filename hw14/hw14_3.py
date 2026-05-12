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

def gdd_season_frist_over200(dates, tavg):
    datasets = []
    for year in range(2001,2023):
        gdd_value = 0
        for i in range(len(dates)):
            if dates[i][0] == year:
                date = dates[i]
                t = tavg[i]
                if date[1] in [4,5,6,7,8,9,10,11,12]:  
                    if t >= 5:      
                        gdd_value += (t - 5)
                        if gdd_value >200:
                            break
        datasets.append(date)               
    return datasets

def main():
    weather_filename = "week10/weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tavg = read_weather_col(weather_filename, 4)
    gdd_over200 = gdd_season_frist_over200(dates, tavg)
    
    for i in range(len(gdd_over200)):
        print(f"{gdd_over200[i][0]} 기준, 4월 이후 누적 적산온도가 200℃에 도달한 첫 번째 날짜는 {gdd_over200[i][1]}월 {gdd_over200[i][2]}일 입니다.")

if __name__=="__main__":
    main()