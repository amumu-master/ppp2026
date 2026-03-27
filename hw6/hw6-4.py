import math
print("각 라디안  sin    cos   tan")
for i in range(91):
    radian= i*math.pi/180
    s=math.sin(radian)
    c=math.cos(radian)
    t=math.tan(radian)
    print(f"{i} {{:.4f}} {{:.4f}} {{:.4f}} {{:.4f}}".format(radian,s,c,t))