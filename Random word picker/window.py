#IMPORTS
import os
import random
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import Frame

_files = open('configs/con1.txt').read().splitlines()
#print(_files)

#DEF
#/Files
def files():
    files = os.listdir('configs')
    #print(files)
    str(files)
    output.configure(state='normal')
    output.insert(INSERT, files)
    output.configure(state='disabled')
    print_files.configure(state='disabled')
    #print(len(files))
    
#def file_open():
#    _open = open('configs/con' + what_file_open.get() + '.txt', 'r')
#    file_contents = _open.read()
#    output.configure(state='normal')
#    output.insert(INSERT, file_contents)
#    output.configure(state='disabled')
    
con_files = 'configs'

def open_con_files():
    os.startfile(con_files, 'open')

#with open("/Users/abc/test.txt", "r") as f:
#    list2 = []
#    for item in f:
#        number = 0
#        while number < 5:
#            list2.append(item + str(number))
#           number += 1
#    print(list2)

#/Buttons
def help():
    output.configure(state='normal')
    output.insert(INSERT, '''\n
To see what files there are, click 'Print Files'. \n
To select a file to display its contents, type the number in the file name in the entry box and press 'This File'.\n
When picking a random word out of the list, input a number in the second entry box that appears, then press the 'times' button.\n
To make a new/different list, click 'Take me to the files', then edit the files you want, making sure you add a new line for each word, then save the file.\n
''')
    output.configure(state='disabled')

def op():
    #def file_open():
    files = os.listdir('configs')
    #files = int(len(files))
    if op.get() == 'Read':
        if what_file_open.get() == '':
            output.configure(state='normal')
            output.insert(INSERT, 'You need to input a number \n')
            output.configure(state='disabled')
        elif what_file_open.get().isdigit() == False:
            output.configure(state='normal')
            output.insert(INSERT, 'You need to input a number \n')
            output.configure(state='disabled')
        elif what_file_open.get().isdigit() == True:
            _open = open('configs/con' + what_file_open.get() + '.txt', 'r')
            file_contents = _open.read()
            output.configure(state='normal')
            output.insert(INSERT, file_contents + '\n')
            output.configure(state='disabled')
    elif op.get() == 'Randomise':
        if what_file_open.get() == '':
            output.configure(state='normal')
            output.insert(INSERT, 'You need to input a number \n')
            output.configure(state='disabled')
        elif what_file_open.get().isdigit() == False:
            output.configure(state='normal')
            output.insert(INSERT, 'You need to input a number \n')
            output.configure(state='disabled')
        try:
            if what_file_open.get().isdigit() == True:
                def amount_rand():
                    amount = int(amount_e.get())
                    #amount = int(amount)
                    for x in range (0, amount):
                        output.configure(state='normal')
                        output.insert(INSERT, random.choice(_list) + '\n')
                        output.configure(state='disabled')
                output.configure(state='normal')
                output.insert(INSERT, 'The words in this list are \n')
                output.configure(state='disabled')
                _open = open('configs/con' + what_file_open.get() + '.txt', 'r')
                _list = open('configs/con' + what_file_open.get() + '.txt').read().splitlines()
                _open = _open.read()
                _open = str(_open)
                output.configure(state='normal')
                output.insert(INSERT, _open + '\n')
                output.configure(state='disabled')
                what_file_open_button.configure(state='disabled')
                what_file_open.configure(state='disabled')
                amount_e = Entry(iframe)
                amount_e.grid(row=2, column=2, padx=5)
                amount_e.focus_set()
                amount_b = Button(iframe, text='Times', command=amount_rand)
                amount_b.grid(row=2, column=3, padx=5)
                
        except IndexError:
            output.configure(state='normal')
            output.insert(INSERT, 'Sorry but that file is empty\n')
            output.configure(state='disabled')
            
    #fix later 
    #elif op.get() == 'Edit':
    #    if what_file_open.get() == '':
    #        output.configure(state='normal')
    #        output.insert(INSERT, 'You need to input a number \n')
    #        output.configure(state='disabled')
    #    elif what_file_open.get().isdigit() == False:
    #        output.configure(state='normal')
    #        output.insert(INSERT, 'You need to input a number \n')
    #        output.configure(state='disabled')
    #    else:
    #        output.configure(state='normal')
    #        output.delete('1.0', END)
    #        output.configure(state='disabled')
    #        what_file_open.configure(state='disabled')
    #        what_file_open_button.configure(state='disabled')
    #        op.configure(state='disabled')
    #        edit = Entry(iframe)
    #        edit.grid(row=2, column=3, padx=5)
    #        edit_enter = Button(iframe, text='Enter', command=change)
    #        edit_enter.grid(row=2, column=4, padx=5)
    #        edit = edit.get
    #        def change():
    #            output.configure(state='normal')
    #           output.insert(INSERT, edit + '\n')

#def test():
#    com = op.get()
#    output.configure(state='normal')
#    output.insert(INSERT, com)
#    output.configure(state='disabled')
    
#TKINTER META
window = Tk()
window.title('Random word picker')
window.resizable(False, False)

#TKINTER FRAMES
iframe = Frame(window)#, highlightbackground="lightgrey", highlightthickness=10, width=100, height=100)
iframe.grid(row=0, column=0, padx=100)
oframe = Frame(window)
oframe.grid(row=0, column=1)

#OFRAME
output = scrolledtext.ScrolledText(oframe, width=60, state='disabled')
output.grid(row=0, column=0)

#IFRAME
#/Buttons
print_files = Button(iframe, text='Print Files', command=files)
print_files.grid(row=0, column=0, pady=5)

link = Button(iframe, text='Take me to the files', command=open_con_files)
link.grid(row=1, pady=5)

what_file_open_button = Button(iframe, text='This file', command=op)
what_file_open_button.grid(row=2, column=1, pady=5)

#style = Style()
#style.configure('redtext', fg='red')
quit = Button(iframe, text='QUIT', command=quit)#, style='redtext')
quit.grid(row=10, pady=5)

help = Button(iframe, text='Help', command=help)
help.grid(row=4, pady=5)

#test = Button(iframe, text='Test', command=test)
#test.grid()

#/Entrys
what_file_open = Entry(iframe)
what_file_open.grid(row=2, column=0, padx=10)

#/Op choose
op = Combobox(iframe)
#op.configure(state='disabled')
op['values']= ('Read', 'Randomise')
op.current(0)
op.grid(row=3, pady=5)