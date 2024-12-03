from tkinter import *
import random

# setting constants
GAMEWIDTH = 600
GAMEHEIGHT = 500
SIZE = 50
PARTS = 3
SNAKECOLOUR = 'GREEN'
FEEDCOLOUR = 'RED'
WINDOWCOLOUR = 'BLACK'
SPEED = 100

class Snake:
    def __init__(self):
        # Initialize snake's body size, coordinates, and parts
        self.bodysize = PARTS
        self.coord = []
        self.squares = []

        # Set initial coordinates for the snake
        for i in range(0, PARTS):
            self.coord.append([0, 0])

        # Draw the initial snake on the canvas
        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=SNAKECOLOUR, tag='snake')
            self.squares.append(square)

class Food:
    def __init__(self):
        # Place food at a random position within the game area
        x = random.randint(0, int(GAMEWIDTH / SIZE - 1)) * SIZE
        y = random.randint(0, int(GAMEHEIGHT / SIZE - 1)) * SIZE
        self.coord = [x, y]

        # Draw the food on the canvas
        canvas.create_oval(x, y, x + SIZE, y + SIZE, fill=FEEDCOLOUR, tag='food')

def next_turn(snake, food):
    x, y = snake.coord[0]

    # Determine the new position based on the current direction
    if direction == 'down':
        y += SIZE
    elif direction == 'right':
        x += SIZE
    elif direction == 'left':
        x -= SIZE
    elif direction == 'up':
        y -= SIZE

    # Insert the new position at the beginning of the snake
    snake.coord.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=SNAKECOLOUR)
    snake.squares.insert(0, square)

    # Check if the snake has eaten the food
    if x == food.coord[0] and y == food.coord[1]:
        global score
        score += 1
        label.config(text=f'Score: {score}')
        canvas.delete('food')
        food = Food()  # Generate new food
    else:
        # Remove the last part of the snake's tail
        del snake.coord[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Check for collisions
    if collision(snake):
        gameover()
    else:
        window.after(SPEED, next_turn, snake, food)

def gameover():
    # Display game over message and show the retry button
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('Arial', 30), text='GAME OVER', fill='red', tags='gameover')
    retry_button.pack()

def collision(snake):
    x, y = snake.coord[0]

    # Check for collision with walls
    if x < 0 or x >= GAMEWIDTH or y < 0 or y >= GAMEHEIGHT:
        return True

    # Check for collision with itself
    for body in snake.coord[1:]:
        if x == body[0] and y == body[1]:
            return True
    return False

def direction_change(side):
    global direction
    # Change direction based on user input, ensuring the snake doesn't reverse
    if side == 'left' and direction != 'right':
        direction = 'left'
    elif side == 'right' and direction != 'left':
        direction = 'right'
    elif side == 'up' and direction != 'down':
        direction = 'up'
    elif side == 'down' and direction != 'up':
        direction = 'down'

def reset_game():
    global score, direction, snake, food
    # Reset game state
    score = 0
    direction = 'down'
    label.config(text=f'Score: {score}')
    canvas.delete(ALL)
    snake = Snake()
    food = Food()
    retry_button.pack_forget()
    next_turn(snake, food)

# Initialize the main window
window = Tk()
window.title('Snake')
#window.resizable(False, False)

# Initialize game variables
score = 0
direction = 'down'

# Create and pack the score label
label = Label(window, font=('Arial', 50), text=f'Score: {score}')
label.pack()

# Create and pack the game canvas
canvas = Canvas(window, bg=WINDOWCOLOUR, width=GAMEWIDTH, height=GAMEHEIGHT)
canvas.pack()

# Create the retry button but do not pack it yet
retry_button = Button(window, text="Retry", font=('Arial', 20), command=reset_game)

# Update window size and center it on the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height+50}+{x}+{y-50}')

# Bind arrow keys for changing direction
window.bind('<Left>', lambda event: direction_change('left'))
window.bind('<Right>', lambda event: direction_change('right'))
window.bind('<Up>', lambda event: direction_change('up'))
window.bind('<Down>', lambda event: direction_change('down'))

# Create the initial snake and food objects
snake = Snake()
food = Food()

# Start the game loop
next_turn(snake, food)

window.mainloop()