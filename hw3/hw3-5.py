#순환하는 반복하는 것들 코딩할 때 나머지(%) 활용
import math
x1=int(input("첫번째 점 x좌표"))
y1=int(input("첫번째 점 y좌표"))
x2=int(input("두번째 점 x좌표"))
y2=int(input("두번째 점 y좌표"))
l=math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
print(f"두 점 사이의 거리:{l}")