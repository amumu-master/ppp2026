def read_rainfall(weather_filename):
    dataset=[]
    with open(weather_filename)as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset   

def count_rainy_days(rainfall):
    datasets = []
    count = 0
    for r in rainfall:
        if r > 0:
            count +=1
        else:
            if count > 0:
                datasets.append(count)
            count = 0
    if count > 0:
        datasets.append(count)
    
    return max(datasets)

def max_rain(rainfall):
    datasets = []
    count=0
    for r in rainfall:
        if r > 0:
           count += r 
        else:
            if count > 0:
                datasets.append(count)
            count = 0
    if count > 0:
        datasets.append(count)
    return max(datasets)

def read_tmax(weather_filename):
    dataset=[]
    with open(weather_filename)as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[3]))
    return dataset

def main():
    rainfall=read_rainfall("week09/weather(146)_2022-2022.csv")
    count_max_rainy_days = count_rainy_days(rainfall)
    rainmax = max_rain(rainfall)
    tmax = read_tmax("week09/weather(146)_2022-2022.csv")
    tmax.sort()
    print(f"최장 연속 강우일수는 {count_max_rainy_days}일 입니다.")
    print(f"강우이벤트 중 최대 강수량은? {(rainmax):.1f}mm 입니다.")
    print(f"가장 더운 날 top3에는 {tmax[-1]}, {tmax[-2]}, {tmax[-3]}도(섭씨) 입니다.")
    
if __name__=="__main__":
    main()