import math
r=float(input("반지름을 입력하시오:"))
s= math.pi*pow(r,2)
l=math.pi*r*2
print(f"원의 둘레는 {{:.1f}}입니다".format(l))
print(f"원의 넓이는 {{:.2f}}입니다.".format(s))