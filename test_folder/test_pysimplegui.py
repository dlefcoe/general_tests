# %% - very simple program

import PySimpleGUI as sg

sg.popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')
sg.popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!', 
    font='Courier 12', text_color='blue', background_color='yellow')


# %% - get a file

import PySimpleGUI as sg

sg.theme('dark')
event, values = sg.Window('Get filename example', 
    [
        [sg.Text('Filename')],
        [sg.Input(), sg.FileBrowse()], 
        [sg.OK(), sg.Cancel()] 
    ]).read(close=True)

print('event:', event)
print('values:', values)





# %% - input box

import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()


