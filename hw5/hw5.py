x=input("변환할 단위를 입력하시오. ")
if x=="화씨":
    temp_f=float(input("화씨 온도를 입력하시오. "))
    temp_c=(temp_f-32)*5/9
    print(f"화씨:{{:.1f}} -> 섭씨:{{:.1f}}".format(temp_f,temp_c))
elif x=="섭씨":
    temp_c=float(input("섭씨 온도를 입력하시오. "))
    temp_f=(temp_c*1.8)+32
    print(f"섭씨:{{:.1f}} -> 화씨:{{:.1f}}".format(temp_c,temp_f))
elif x=="피트" or x=="ft":
    ft=float(input("길이를 입력하시오(ft). "))
    cm=ft*30.48
    print(f"ft:{{:.1f}} -> cm:{{:.1f}}".format(ft,cm))
elif x=="센티미터" or x=="cm":
    cm=float(input("길이를 입력하시오(cm). "))
    ft=cm/30.48
    print(f"cm:{{:.1f}} -> ft:{{:.1f}}".format(cm,ft))

