def caesar_encode(a):    #소문자 97-122 대문자 65-90
    if ord(a) >= 65 and ord(a) <= 87 :
        return chr(ord(a) + 3)
    if ord(a) > 87 and ord(a) <= 90 :
        return chr(ord(a) - 25)       
    if ord(a) >= 97 and ord(a) <= 119:
        return chr(ord(a) + 3)
    if ord(a) > 119 and ord(a) <= 122:
        return chr(ord(a) - 25)

def toggle_text(text):
    result = ""
    for c in text:
        result += caesar_encode(c)
    return result

def main():
    a =  input("단어를 입력하세요. 암호로 변환해 드립니다. ")
    code = toggle_text((a))
    print(f"암호는 {code} 입니다.")

if __name__=="__main__":
    main()