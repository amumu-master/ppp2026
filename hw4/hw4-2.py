import math
x=int(input("x좌표 : "))
y=int(input("y좌표 : "))

if x>0 and y>0:
    print(f"입력한 좌표 {(x,y)}는 1사분면입니다.")
elif x<0 and y>0:
    print(f"입력한 좌표 {(x,y)}는 2사분면입니다.")    
elif x<0 and y<0:
    print(f"입력한 좌표 {(x,y)}는 3사분면입니다.")
elif x>0 and y<0:
    print(f"입력한 좌표 {(x,y)}는 4사분면입니다.")
elif x==0 and y==0:
    print(f"입력한 좌표 {(x,y)}는 원점입니다.")
elif x==0 :
    print(f"입력한 좌표 {(x,y)}는 y축에 있습니다.")
elif y==0 :
    print(f"입력한 좌표 {(x,y)}는 x축에 있습니다.")

