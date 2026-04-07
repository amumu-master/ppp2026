def is_leap_year(y):
    if y%4 == 0 and y%100 != 0:
        return True
    else:
        return False

def main():
    x=int(input("몇 년도니? "))
    if is_leap_year(x):
        print(f"{x}년도는 윤년입니다")
    else:
        print(f"{x}년도는 윤년이 아닙니다.")

if __name__=="__main__":
    main()