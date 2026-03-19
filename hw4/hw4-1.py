import math
w=float(input("몸무게(kg)를 입력하시오:")) 
h=float(input("키(cm)를 입력하시오:"))*0.01
bmi=w/pow(h,2)
print(f"당신의 BMI 지수는 {bmi} 입니다.")
if bmi<25:
    print("당신은 비만 전단계입니다.")
elif bmi<30:
    print("당신은 비만 1단계입니다.")
elif bmi<35:
    print("당신은 비만 2단계입니다.")
else :
    print("당신은 비만 3단계입니다.")
