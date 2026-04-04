cal_dict = { '한라봉': 50, '딸기': 34, '바나나': 77}
eat_dict = {'한라봉':100,'딸기': 200, '바나나': 500}

total_cal = 0
for key,val in eat_dict.items():
    print(key,val)
    if key in cal_dict:
        total_cal +=val*cal_dict[key]
print(f"총 섭취 칼로리는 {total_cal}입니다.")