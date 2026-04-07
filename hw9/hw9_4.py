def average(nums):
    aver=sum(nums)/len(nums)
    return aver

def main():
    text=input("숫자들을 쉼표(,)로 구분해서 입력하세요. :")
    x=text.split(",")
    nums=[]
    for i in x:     
        nums.append(int(i))
    print(f"{nums}의 평균은 {average(nums)}입니다.")

if __name__=="__main__":
    main()