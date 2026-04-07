nums=[1,2,3,4,5]

def average(nums):
    aver=sum(nums)/len(nums)
    return aver

def main():
    print(f"{nums}의 평균은 {average(nums)}입니다.")

if __name__=="__main__":
    main()