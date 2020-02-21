from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *

window = Tk()
window.title('Leap year checker')
window.resizable(False, False)

'''
output.configure(state='normal')
output.insert(INSERT, '')
output.configure(state='disabled')
'''

def _help():
    output.configure(state='normal')
    output.insert(INSERT, '''INSTRUCTIONS:

Type the year you want to count *from* in the first entry box, then press the button labled 'This Year' nex to that entry box
Then type the year you want to count to in the second
Then, if you only want to display either leap years or non-leap years, click the one you want, respectivly, but if you want to display both, click 'Both'
**WARNING**
If possible, try not to use a big gap between the starting and end year, since it can take a while to finish.
If you do however make to big a gap and its taking to long or taking to many system resources, just X out of the program, or press the 'Quit' button.
----------------------------------------''')
    output.configure(state='disabled')
    help.configure(state='disabled')
    
def quit_b():
    window.destroy()

def test():
    output.configure(state='normal')
    output.insert(INSERT, selected.get())
    output.insert(INSERT, num1.get())
    output.configure(state='disabled')

def year1():
    year1 = num1.get()
    #year1 = int(year1)
    if year1.isdigit() == True:
        year1 = str(year1)
        output.configure(state='normal')
        output.insert(INSERT, 'Between ' + year1)
        output.configure(state='disabled')
        num1.configure(state='disabled')
        num2.configure(state='normal')
        butt1.configure(state='disabled')
        butt2.configure(state='normal')
        help.configure(state='disabled')
        num2.focus_set()
        return year1
    #elif year1.isdigit == False:
        #output.configure(state='normal')
        #output.insert(INSERT, 'Sorry but you neeed to input a number')
        #output.configure(state='disabled')

def year2():
    year2 = num2.get()
    if year2.isdigit() == True:
        year2 = str(year2)
        output.configure(state='normal')
        output.insert(INSERT, ' and ' + year2 + ' \n')
        output.configure(state='disabled')
        num2.configure(state='disabled')
        butt2.configure(state='disabled')
        ly.configure(state='normal')
        nly.configure(state='normal')
        both.configure(state='normal')
      
def _rad():
    final.configure(state='enabled')
    
def _final():
    ly.configure(state='disabled')
    nly.configure(state='disabled')
    both.configure(state='disabled')
    final.configure(state='disabled')

iframe = Frame(window)
iframe.grid(row=0, column=0, padx=25)
tframe = Frame(window)
tframe.grid(row=0, column=1)

wel = Label(iframe, text='''Welcome to my
leap year checker''',font=100)
wel.grid(row=0, columnspan=2, pady=(0,0))

between = Label(iframe, text='Between')
between.grid(row=2)

help = Button(iframe, text='Help', command=_help)
help.grid(row=1, columnspan=2, pady=10)

butt1 = Button(iframe, text='This year', command=year1)
butt1.grid(row=3, column=1)

num1 = Entry(iframe, text='test')
num1.grid(row=3, column=0)
num1.focus_set()

_and = Label(iframe, text='and')
_and.grid(row=4)

output = scrolledtext.ScrolledText(tframe, width=40)
output.grid(row=0, column=0)

num2 = Entry(iframe, state='disabled')
num2.grid(row=5, column=0)

butt2 = Button(iframe, text='This year', command=year2, state='disabled')
butt2.grid(row=5, column=1)

#----------------------------------------------------------------------------

def op():
    ly.configure(state='disabled')
    nly.configure(state='disabled')
    both.configure(state='disabled')
    rad = selected.get()
    a = int(num1.get())
    b = int(num2.get())
    for x in range(a, b):
        x = x + 1
        if rad == 1:
            if x % 4 == 0:
                #does leap years
                x = str(x)
                output.configure(state='normal')
                output.insert(INSERT, x + ' is a leap year  \n')
                output.configure(state='disabled')
        elif rad == 2:
            if x % 4 != 0:
                #does non leap years
                x = str(x)
                output.configure(state='normal')
                output.insert(INSERT, x + ' isn\'t a leap year  \n')
                output.configure(state='disabled')
        elif rad == 3:
            if x % 4 == 0:
                x = str(x)
                output.configure(state='normal')
                output.insert(INSERT, x + ' is a leap year  \n')
                output.configure(state='disabled')
            elif x % 4 != 0:
                #does both
                x = str(x)
                output.configure(state='normal')
                output.insert(INSERT, x + ' isn\'t a leap year  \n')
                output.configure(state='disabled')
         
#----------------------------------------------------------------------------

selected = IntVar()

rbl = Label(iframe, text='Would you like to only display leap years, non-leap years or both')
rbl.grid(row=6, pady=10, columnspan=2)

ly = Radiobutton(iframe, text='Leap years only', value=1, variable=selected, state='disabled', command=_rad)
ly.grid(row=7, column=0)

nly = Radiobutton(iframe, text='Non-leap years only', value=2, variable=selected, state='disabled', command=_rad)
nly.grid(row=7, column=1)

both = Radiobutton(iframe, text='Both', value=3, variable=selected, state='disabled', command=_rad)
both.grid(row=8, columnspan=2)

final = Button(iframe, text='Click here to calculate!', command=op, state='disabled')
final.grid(row=9, columnspan=2, pady=(10,0))

_quit = Button(iframe, text='QUIT', command=quit_b)
_quit.grid(columnspan=2, pady=(10,0))

window.mainloop()
