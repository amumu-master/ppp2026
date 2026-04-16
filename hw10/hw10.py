def average(nums):
    return sum(nums)/len(nums)

def read_text(filename):
    with open(filename) as f:
        text = f.readline()
    return text

def text2list(text):
    numbers=[]
    for i in text.split():
        numbers.append(int(i))
    return numbers
        
def median(x):
    if len(x)%2==0:
        h = len(x)//2
        e = (x[h-1]+x[h])/2
        return e
    else : 
        return x[len(x)/2 + 0.5]

def median(x):
    if len(x)%2==0:
        h = len(x)//2
        e = (x[h-1]+x[h])/2
        return e
    else : 
        return x[len(x)//2]

def main():
    text = read_text("week07/numbers1.txt")
    num_list = text2list(text)
    num_list.sort()
    print(num_list)
    print(f"숫자의 개수 : {len(num_list)}")
    print(f"주어진 숫자의 평균 : {average(num_list)}")
    print(f"주어진 숫자의 최댓값 : {max(num_list)}")
    print(f"주어진 숫자의 최솟값 : {min(num_list)}")
    print(f"주어진 숫자의 중앙값 : {median(num_list)}")
    
if __name__=="__main__":
    main()