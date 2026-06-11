import PySimpleGUI as sg
import random

def make_lotto(n):
    result = []
    for _ in range(n):
        nums = random.sample(range(1, 46), 6)
        nums.sort()
        result.append(nums)
    return result

layout = [
    [sg.Text("로또 번호 생성기", font=("Arial", 14, "bold"), justification="center", expand_x=True)],
    [sg.Text("몇 장?", size=(6,1)), sg.Input("1", key="-CNT-", size=(5,1)), sg.Button("생성", size=(8,1))],
    [sg.Text("─" * 38)],
    [sg.Multiline("", key="-RESULT-", size=(38, 10), disabled=True, font=("Courier", 12))],
    [sg.Button("초기화", size=(10,1)), sg.Button("종료", size=(10,1))],
]

window = sg.Window("hw21_4 | 로또 생성기", layout, size=(340, 300), finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "종료"):
        break

    if event == "생성":
        cnt_str = values["-CNT-"].strip()
        if not cnt_str.isdigit() or int(cnt_str) < 1:
            sg.popup("1 이상의 숫자를 입력하세요!", title="입력 오류")
            continue
        cnt = int(cnt_str)
        tickets = make_lotto(cnt)
        lines = []
        for i, t in enumerate(tickets, 1):
            lines.append(f"{i:2d}번: {' '.join(f'{n:2d}' for n in t)}")
        window["-RESULT-"].update("\n".join(lines))

    if event == "초기화":
        window["-RESULT-"].update("")
        window["-CNT-"].update("1")

window.close()
