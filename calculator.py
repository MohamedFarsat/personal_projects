from tkinter import*


#Function that is called when each button is pressed. Adds the value to a string and updates the String Variable
def press(number):
    global equation
    equation += str(number)
    label_update.set(equation)

#Function that clears the label
def clear():
    global equation
    label_update.set('')
    equation = ''

#Function that evaluates the equation and displays the total calculated value. Checks for errors as well.
def equal():
    global equation
    try:
        total = str(eval(equation))
        label_update.set(total)
        equation = total
    except (UnboundLocalError,SyntaxError):
        if label_update.get() == '':
            label_update.set('No inputs given, please try again')
        else:
            label_update.set('Syntax error, please try again')
        equation = ''
    except (ZeroDivisionError):
        label_update.set('Arithmatic error, please try again')
        equation = ''

#Function that allows users to delete charecters from the label
def backspace():
    global equation
    equation = equation[:-1]
    label_update.set(equation)


window= Tk()
window.config(bg='grey')
window.title('CALCULATOR')

#setting an empty string and String Variable for values to be added to.
equation = ''
label_update = StringVar()

#Display for calculator
label = Label(window,textvariable=label_update,width=31,height=5,bg='black',fg='white')
label.pack()

#Frame for the buttons to be added to
frame = Frame(window)
frame.pack()

#Loop to create buttons 0-9
buttons = []
for i in range(10):
    button = Button(frame,text=i,command= lambda i=i: press(i),width=5,height=5)
    buttons.append(button)

buttons[1].grid(row=0, column=0) 
buttons[2].grid(row=0, column=1) 
buttons[3].grid(row=0, column=2) 
buttons[4].grid(row=1, column=0) 
buttons[5].grid(row=1, column=1) 
buttons[6].grid(row=1, column=2) 
buttons[7].grid(row=2, column=0) 
buttons[8].grid(row=2, column=1) 
buttons[9].grid(row=2, column=2) 
buttons[0].grid(row=3, column=1)

#Creating buttons for operators etc
plus = Button(frame,text='+',command = lambda:press('+'),width=5,height=5)
minus = Button(frame,text='-',command = lambda:press('-'),width=5,height=5)
times = Button(frame,text='x',command = lambda:press('*'),width=5,height=5)
divide = Button(frame,text='÷',command = lambda:press('/'),width=5,height=5)
dot = Button(frame,text='.',command = lambda:press('.'),width=5,height=5)
clear = Button(frame,text='clear',command = clear,width=5,height=5)
equal = Button(frame,text='=',command = equal,width=5,height=11)
backspace = Button(frame,text='DEL',command = backspace,width=5,height=11)

plus.grid(row=0,column=3)
minus.grid(row=1,column=3)
times.grid(row=2,column=3)
divide.grid(row=3,column=3)
clear.grid(row=3,column=0)
dot.grid(row=3,column=2)
backspace.grid(row=0,column=4,rowspan=2)
equal.grid(row=2,column=4,rowspan=2)


window.mainloop()