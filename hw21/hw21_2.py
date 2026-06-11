import PySimpleGUI as sg
import random

def new_question():
    a = random.randint(2, 9)
    b = random.randint(1, 9)
    return a, b

score = 0
count = 0
a, b = new_question()

layout = [
    [sg.Text("구구단 퀴즈", font=("Arial", 14, "bold"), justification="center", expand_x=True)],
    [sg.Text("", key="-QUESTION-", font=("Arial", 18), justification="center", expand_x=True)],
    [sg.Text("정답:", size=(5,1)), sg.Input(key="-ANS-", size=(10,1), focus=True), sg.Button("확인", bind_return_key=True)],
    [sg.Text("", key="-RESULT-", font=("Arial", 12), justification="center", expand_x=True)],
    [sg.Text("진행:", size=(5,1)), sg.Text("0 / 10", key="-PROG-")],
    [sg.Text("점수:", size=(5,1)), sg.Text("0", key="-SCORE-", font=("Arial", 12, "bold"))],
    [sg.Button("종료", size=(10,1))],
]

window = sg.Window("hw21_2 | 구구단 퀴즈", layout, size=(320, 260), finalize=True)
window["-QUESTION-"].update(f"{a}  ×  {b}  =  ?")

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "종료"):
        break

    if event == "확인":
        ans = values["-ANS-"].strip()
        if not ans.lstrip("-").isdigit():
            window["-RESULT-"].update("숫자를 입력하세요", text_color="orange")
            continue

        count += 1
        if int(ans) == a * b:
            score += 10
            window["-RESULT-"].update("✓ 정답!", text_color="green")
        else:
            window["-RESULT-"].update(f"✗ 오답 (정답: {a*b})", text_color="red")

        window["-SCORE-"].update(str(score))
        window["-PROG-"].update(f"{count} / 10")
        window["-ANS-"].update("")

        if count >= 10:
            sg.popup(f"퀴즈 종료!\n총 점수: {score}점", title="결과")
            score = 0
            count = 0
            window["-SCORE-"].update("0")
            window["-PROG-"].update("0 / 10")
            window["-RESULT-"].update("")

        a, b = new_question()
        window["-QUESTION-"].update(f"{a}  ×  {b}  =  ?")

window.close()
