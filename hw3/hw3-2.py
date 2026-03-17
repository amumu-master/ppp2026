import math
w=float(input("몸무게(kg)를 입력하시오:")) 
h=float(input("키(cm)를 입력하시오:"))*0.01
bmi=w/pow(h,2)
print(f"당신의 BMI 지수는 {bmi} 입니다.")