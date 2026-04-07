cal_dict = { '한라봉': 50, '딸기': 34, '바나나': 77}
eat_dict = {'한라봉':100,'딸기': 200, '바나나': 500}
def cal():
    total_cal = 0
    for key,val in eat_dict.items():
        if key in cal_dict:
            total_cal +=val*cal_dict[key]
    return total_cal
def main():
    print(f"총 섭취 칼로리는 {cal()}입니다.")

if __name__=="__main__":
    main()