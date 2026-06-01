import random

def random_number(n):
    num_list=[]
    for i in range(n):
        x=[]
        while True:
            i = random.randint(1,45)
            if i not in x :
                x.append(i)
            if len(x) == 6:
                break
        num_list.append(x)
    return num_list
 
def main():
    frequency = int(input("로또 몇 장 살꺼야? "))
    num=random_number(frequency)
    print(num)
if __name__=="__main__":
    main()