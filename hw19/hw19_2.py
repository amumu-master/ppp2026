import random

def gugudan_correct():
    a = random.randint(2,9)
    b = random.randint(1,9)
    ans = input(f"{a} * {b} = ? ")
    return int(ans) == a*b

def main():
    score = 0 
    for i in range(10):
        if gugudan_correct():
            score += 10
    print(f"총 점수는  {score}점 입니다.")        

if __name__=="__main__":
    main()