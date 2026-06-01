import random
# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

words = ["사과", "수박", "딸기", "참외", "메론"]

def random_word():
    a = random.randint(0,len(words)-1)
    return words[a]

def to_chosung(text):
    chosung_str=""
    for c in text:
        x = int((ord(c)-44032)/588)
        chosung_str += CHOSUNG_LIST[x]
    return chosung_str

def chosung_correct(text):
    ans = input("정답을 말해보세요. ")
    while True:
        if text != ans:
            ans=input("다시 시도해 보세요. ")
        else:
            print("정답입니다!")
            break

def main():
    text = random_word()
    CHO = to_chosung(text)
    print(f"초성은 {CHO}입니다.")
    chosung_correct(text)
    
if __name__=="__main__":
    main()