x=int(input("한라봉 섭취량(g) : "))
y=int(input("딸기(설향) 섭취량(g) : "))
z=int(input("바나나 섭취량(g) : "))
x_c= x*50/100
y_c= y*34/100
z_c= z*77/100
c=x_c+y_c+z_c
print(f"한라봉 {x_c}칼로리, 딸기(설향) {y_c}칼로리, 바나나 {z_c}칼로리")
print(f"총 {c}칼로리 섭취했습니다.")