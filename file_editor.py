import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

# Function to change the text color
def change_color():
    color = colorchooser.askcolor(title='Pick a colour')
    text_area.config(fg=color[1])

# Function to change the font style and size
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

# Function to create a new file
def new_file():
    window.title('Untitled')
    text_area.delete('1.0', END)

# Function to open an existing file
def open_file():
    file = askopenfile(defaultextension=".txt",
                       filetypes=[('All files', '*.*'),
                                  ('Text Documents', '*.txt')])
    if file is not None:
        try:
            window.title(os.path.basename(file.name))
            text_area.delete('1.0', END)
            
            with open(file.name, 'r') as filecontents:
                text_area.insert(1.0, filecontents.read())
        except Exception as e:
            print('Cannot read file', e)

# Function to save the current file
def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                        defaultextension='.txt',
                                        filetypes=[('All files', '*.*'), ('Text Documents', '*.txt')])
    
    if file is not None:
        try:
            window.title(os.path.basename(file))
            with open(file, 'w') as line:
                line.write(text_area.get('1.0', END))
        except Exception as e:
            print('Could not save file', e)

# Function to cut selected text
def cut():
    text_area.event_generate('<<Cut>>')

# Function to copy selected text
def copy():
    text_area.event_generate('<<Copy>>')

# Function to paste text from clipboard
def paste():
    text_area.event_generate('<<Paste>>')

# Function to show information about the program
def about():
    showinfo('About this program', 'This is a program written by Farsat. You can open and edit existing files, or create new files.')

# Initialize the main window
window = Tk()
window.title('Text editor')
file = None

# Set window dimensions
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the center position of the window
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Set the geometry of the window
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Variables for font name and size
font_name = StringVar(window)
font_name.set('Arial')

font_size = StringVar(window)
font_size.set('25')

# Create the text area
text_area = Text(window, font=(font_name.get(), font_size.get()))

# Add a scroll bar to the text area
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

# Create a frame for additional controls
frame = Frame(window)
frame.grid()

# Button to change text color
color_button = Button(frame, text='color', command=change_color)
color_button.grid(row=0, column=0)

# Dropdown menu to select font family
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

# Spinbox to select font size
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# Create a menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Paste', command=paste)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label="About", command=about)

# Run the application
window.mainloop()
