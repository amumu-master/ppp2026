def str2int(text: str,default_value: int=-999):
    try:
            return int(text)
    except ValueError:
            return default_value

def x_append():    
    values=[]
    while True:
        x = input("x => ? ")
        x_value = str2int(x) #정수 or None
        if x_value ==-1:
            break
        if x_value > 0:
            values.append(x_value)
    return values
def main():
    x_list = x_append()
    print(x_list)
    print(f"개수 : {len(x_list)}개")
    print(f"평균 : {sum(x_list)/len(x_list)}")
if __name__=="__main__":
    main()