def c2f(t_c):
    t_f = t_c*1.8 +32
    return t_f

def main():
    x=float(input("몇 도야?(섭씨)"))
    print(f"섭씨 :{x} -> 화씨 : {c2f(x)}")

if __name__=="__main__":
    main()