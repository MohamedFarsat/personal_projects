from tkinter import*


turn = 0 # To alternate between 0 and 1 to determine which player's turn it is

xcount = [] 
ocount = []

values_to_check = [(0,1,2),# Each square is marked as a number from 0 to 8. The below sets of values are the winning values
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6)]

tries = 0 # used to check if the game is a tie

def press(number): # function that is called each time a square is pressed
    global turn
    global tries
    if turn ==0:
        buttons[number].config(text='X',state=DISABLED,font=('Arial', 24), height=2, width=5) # The marker is input into the button and the button is disabled
        turn += 1 # to switch turns
        xcount.append(number)
        if checker(xcount):  # To check if there is a winning sequence
            show_winner('X')
            for i in range(9):
                buttons[i].config(state=DISABLED)
            return
    else:
        buttons[number].config(text='O',state=DISABLED,font=('Arial', 24), height=2, width=5)
        turn-=1
        ocount.append(number)
        if checker(ocount):
            show_winner('O')
            for i in range(9):
                buttons[i].config(state=DISABLED)
            return
    tries +=1
    if tries == 9:
        label.config(text='It is a draw!') # check for a tie

def show_winner(letter): # function that inputs the winner into the label
    label.config(text=f'{letter} wins!') 

def checker(count): # To check if there is a winning sequence
    for i in values_to_check:
        win = all(value in count for value in i)
        if win:
            return win

def reset(): #resets game
    global turn 
    global xcount
    global ocount
    global tries
    tries = 0
    turn = 0
    xcount = []
    ocount = []
    for i in range(9):
        buttons[i].config(text='',state=NORMAL)
    label.config(text='')

window = Tk()
window.title('Tic-Tac-Toe')


frame = Frame(window,padx=10,pady=10)
frame.pack()

buttons = [] 
for i in range(9): # creates the squares packs them in a 3x3 format
    button = Button(frame,font=('Arial', 24),command= lambda i=i:press(i),width=5,height=2)
    buttons.append(button)
    button.grid(row=i//3,column=i%3)


frame2 = Frame(window)
frame2.pack()
exit = Button(frame2,width=10,height=5,text='Exit',command=quit)
exit.grid(row=0,column=0)

retry = Button(frame2,width=10,height=5,text='Retry',command=reset)
retry.grid(row=0,column=1)

label = Label(window,font=('Arial','40'),bd=5)
label.pack()

window.mainloop()