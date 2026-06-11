# hw21_3.py - 단어 맞추기 게임 (PySimpleGUI)
import PySimpleGUI as sg
import random

WORDS = ['apple', 'people', 'mouse', 'bottle', 'phone', 'book']

def new_game():
    word = list(random.choice(WORDS))
    hidden = ["_"] * len(word)
    return word, hidden

word, hidden = new_game()
trials = len(word)

def display(hidden):
    return "  ".join(hidden)

layout = [
    [sg.Text("단어 맞추기", font=("Arial", 14, "bold"), justification="center", expand_x=True)],
    [sg.Text(display(hidden), key="-WORD-", font=("Courier", 22, "bold"), justification="center", expand_x=True)],
    [sg.Text("남은 기회:", size=(8,1)), sg.Text(str(trials), key="-TRIAL-", font=("Arial", 12, "bold"), text_color="red")],
    [sg.Text("글자 입력:", size=(8,1)), sg.Input(key="-LETTER-", size=(5,1)), sg.Button("입력", bind_return_key=True)],
    [sg.Text("", key="-MSG-", justification="center", expand_x=True)],
    [sg.Button("새 게임", size=(10,1)), sg.Button("종료", size=(10,1))],
]

window = sg.Window("hw21_3 | 단어 게임", layout, size=(340, 220), finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "종료"):
        break

    if event == "새 게임":
        word, hidden = new_game()
        trials = len(word)
        window["-WORD-"].update(display(hidden))
        window["-TRIAL-"].update(str(trials))
        window["-MSG-"].update("")
        window["-LETTER-"].update("")

    if event == "입력":
        letter = values["-LETTER-"].strip().lower()
        window["-LETTER-"].update("")

        if len(letter) != 1 or not letter.isalpha():
            window["-MSG-"].update("한 글자(알파벳)만 입력하세요", text_color="orange")
            continue

        hit = False
        for i in range(len(word)):
            if word[i] == letter:
                hidden[i] = letter
                hit = True

        if not hit:
            trials -= 1
            window["-TRIAL-"].update(str(trials))
            window["-MSG-"].update(f"'{letter}' 없음!", text_color="red")
        else:
            window["-MSG-"].update(f"'{letter}' 있음!", text_color="green")

        window["-WORD-"].update(display(hidden))

        if hidden == word:
            sg.popup(f"정답! {''.join(word)}", title="성공 🎉")
            word, hidden = new_game()
            trials = len(word)
            window["-WORD-"].update(display(hidden))
            window["-TRIAL-"].update(str(trials))
            window["-MSG-"].update("")
        elif trials <= 0:
            sg.popup(f"실패! 정답은 {''.join(word)}", title="게임 오버")
            word, hidden = new_game()
            trials = len(word)
            window["-WORD-"].update(display(hidden))
            window["-TRIAL-"].update(str(trials))
            window["-MSG-"].update("")

window.close()
