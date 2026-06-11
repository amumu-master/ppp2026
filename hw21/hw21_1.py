# hw21_1.py - 카운트다운 타이머 (PySimpleGUI)
import PySimpleGUI as sg
import time

layout = [
    [sg.Text("카운트다운 타이머", font=("Arial", 14, "bold"), justification="center", expand_x=True)],
    [sg.Text("10", key="-COUNT-", font=("Arial", 48, "bold"), justification="center", expand_x=True, text_color="red")],
    [sg.Button("시작", size=(10, 1)), sg.Button("종료", size=(10, 1))],
]

window = sg.Window("hw21_1 | 카운트다운", layout, size=(300, 200), finalize=True)

while True:
    event, _ = window.read(timeout=100)
    if event in (sg.WIN_CLOSED, "종료"):
        break

    if event == "시작":
        for i in range(10, 0, -1):
            window["-COUNT-"].update(str(i))
            window.refresh()
            time.sleep(1)
        window["-COUNT-"].update("끝!")
        sg.popup("카운트다운 완료!", title="완료")
        window["-COUNT-"].update("10")

window.close()
