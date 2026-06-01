import random
words=['apple','people','mouse','bottle','phone','book']

def random_word():
    x = random.choice(words)
    word=[]
    for i in x:
        word.append(i)
    return word

def _list(word):
    empty = []
    for i in range(len(word)):
        empty.append("_")
    return empty

def _toword(word,empty):
    x = len(word)
    while True:
        if x==0:
            print("더 이상 기회가 없습니다.")
            break
        if word == empty:
            print(f"{" ".join(empty)} 정답입니다.")
            break
        ans = input(f"{" ".join(empty)}(trial={x}) 답을 입력하시오. =>")
        if ans=="break":
            break
        if not len(ans)==1:
            print("한 글자만 입력해주세요.") 
            ans = input(f"{" ".join(empty)}(trial={x}) 답을 입력하시오. =>")

        for i in range(len(word)):
            if word[i] == ans:
                empty[i] = ans
        if ans not in word:
            x = x-1
       
    return empty

def main():
    word = random_word()
    empty = _list(word)
    _toword(word,empty)
    
if __name__=="__main__":
    main()