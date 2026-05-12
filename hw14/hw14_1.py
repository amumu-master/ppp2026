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

def get_max_diff(dates, tmax, tmin):
    datasets=[]
    for year in range(2001,2023):
        max_diff = -999
        max_diff_date = None
        for i in range(len(dates)):
            if dates[i][0] == year:    
                diff = tmax[i]-tmin[i]
                if diff >max_diff:
                    max_diff =  diff
                    max_diff_date = dates[i]
        datasets.append([max_diff_date, round(max_diff, 1)])
    return datasets

def main():
    weather_filename = "week10/weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename, 3)
    tmin = read_weather_col(weather_filename, 5)
    max_diff = get_max_diff(dates, tmax, tmin)
    for i in range(len(max_diff)):
        print(f"{max_diff[i][0][0]}년도의 일교차가 가장 큰 날은 {max_diff[i][0][1]}월 {max_diff[i][0][2]}일이고, 일교차는{max_diff[i][1]}도 입니다.")

if __name__=="__main__":
    main()