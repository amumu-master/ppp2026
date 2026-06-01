def toggle_ch(a):
    if ord(a) >= 65 and ord(a) <= 90 : 
       return chr(ord(a) + 32)
    elif ord(a) >= 97 and ord(a) <= 122:
        return chr(ord(a) - 32)
    
def toggle_text(text):
    result = ""
    for c in text:
        result += toggle_ch(c)
        # result = result + toggle_ch(c)
    return result

def main():
    x = input("단어를 입력하세요 대소문자를 바꿔드립니다. ") 
    print(toggle_text(x))

if __name__=="__main__":
    main()