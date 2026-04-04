mart = {"우유": 2800, "계란": 300, "빵": 1200, "물": 1700}
cart = ["우유", "우유", "계란", "계란", "계란"]
#cart = ["계란", "빵"]

total_cost=0
for item in cart:
    total_cost +=mart[item]
print(f"우유 {cart.count("우유")}개, 계란 {cart.count("계란")}개 로")
print(f"물건 총 금액은 {total_cost}원 입니다.")
#print("총 구매금액은 {:,}원입니다.".format(total_cost))
