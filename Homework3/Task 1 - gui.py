# Task 1 Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

import PySimpleGUI as sg

layout = [[sg.Text("Введіть рандомне слово: ")],
            [sg.Input(key='-INPUT-Word')],
            [sg.Text("Введіть номер символу: ")],
            [sg.Input(key='-INPUT-Number')],
            [sg.Text(size=(40,2), key='-OUTPUT-')],
            [[sg.Button('Ok'), sg.Button('Quit')]]
            ]


window = sg.Window('Find your letter', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    expected_number = values['-INPUT-Number']
    expected_word = values['-INPUT-Word']

    if not expected_number.isnumeric():
        window['-OUTPUT-'].update("Поле номеру повинно містити тільки цифри!!!")
    elif expected_word.isspace():
        window['-OUTPUT-'].update("Поле слова не може містити лише пробіли!!!")
    elif len(expected_word) < 1:
        window['-OUTPUT-'].update("Поле слова не може бути пустим!!!")
    elif int(expected_number) > len(expected_word):
        window['-OUTPUT-'].update("Цифра повинна бути менша чим кількість букв в слові!!!")
    elif int(expected_number) < 1:
        window['-OUTPUT-'].update("Цифра повинна бути не менша 1!!!")
    else:
        window['-OUTPUT-'].update('Твоя буква є: ' + expected_word[int(expected_number)-1])
window.close()
