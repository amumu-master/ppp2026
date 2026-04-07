def sum_n(n):
    t=0
    for i in range(1,n+1):
        t+=i
    return t

def main():
    x=int(input("1부터 몇까지 더할거야? "))
    print(sum_n(x))

if __name__=="__main__":
    main()