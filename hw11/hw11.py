def read_rainfall(weather_filename):
    dataset=[]
    with open(weather_filename)as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset   

def read_tagv(weather_filename):
    dataset=[]
    with open(weather_filename)as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[4]))
    return dataset

def get_days_over_5mm(x):                                             
    over_5mm=[]
    for i in x:
        if i>=5:
            over_5mm.append(i)
    return over_5mm
#[x for x in rainfall if x >= 5]

def main():
    tavg=read_tagv("week09/weather(146)_2022-2022.csv")
    rainfall=read_rainfall("week09/weather(146)_2022-2022.csv")
    print(f"연 평균 온도는 {sum(tavg)/len(tavg):.1f}")
    print(f"연 평균 강수량은 {sum(rainfall)}")
    print(f"5mm이상 강우일수는 {len(get_days_over_5mm(rainfall))}일 입니다")

if __name__=="__main__":
    main()