import PySimpleGUI as sg

sg.theme('DarkAmber') # Modern colors
layout = [ [sg.Text('DemoText, Hello World')],
           [sg.Text('Row2 Input'), sg.InputText()],
           [sg.Button('Ok'), sg.Button('Cance')]   ]

window = sg.Window('Window Jabroni', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You Entered ', values[0])

window.close()