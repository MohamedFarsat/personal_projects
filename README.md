This section of the repository includes four different applications: Snake game, Tic-Tac-Toe game, Text-editor, and Calculator. Each project is designed to showcase different aspects of Python programming and GUI development using Tkinter.


# Snake Game
The Snake game is a classic arcade game implemented using Python and Tkinter. The objective of the game is to control the snake to eat food, grow longer, and avoid collisions with the walls and its own body.

## Features
- Control the snake using the arrow keys.

- Randomly placed food items.

- Score tracking based on the number of food items eaten.

- Game over screen with a retry button.


# Tic-Tac-Toe Game
The Tic-Tac-Toe game is a simple two-player game implemented using Python and Tkinter. Players take turns to mark their symbol (X or O) on a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Features
- 3x3 grid for the game

- Player turn indication

- Automatic winner detection

- Game reset functionality


# Text-editor
The Text-editor is a basic text editing application implemented using Python and Tkinter. It allows you to create, open, edit, and save text files, with additional features to customize the text appearance.

## Features
- Change text color.

- Change font and size.

- Create new files, open existing files, and save files.

- Cut, copy, and paste functionality.


# Calculator
The Calculator is a basic application implemented using Python and Tkinter. It allows you to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features
- Support for addition, subtraction, multiplication, and division.

- Clear and delete functionality.

- Error handling for invalid inputs

<br/>

# Comprehensive Number Validator: IMEI, ISBN, UPC, and Credit Card Validator

This Python program validates various types of identification numbers using different algorithms. The program prompts the user to input a number and select the type of number to validate. Supported number types include IMEI, ISBN-10, ISBN-13, Universal Product Code (UPC), and major credit card numbers (Visa, MasterCard, Amex). The program implements the Luhn algorithm for certain types of numbers and specific checksum calculations for others to ensure the validity of the provided numbers.

## Features:

- Validate IMEI numbers.

- Validate ISBN-10 and ISBN-13 numbers.

- Validate Universal Product Codes (UPC).

- Validate Visa, MasterCard, and American Express credit card numbers using the Luhn algorithm.

- User-friendly prompts and error handling for invalid inputs.

## Requirements for each type of number to be valid with samples:

### IMEI Number
- Length: 15 digits
- Validation: Luhn algorithm
- Sample: 490154203237518 (Valid IMEI)

### ISBN-10 Number
- Length: 10 digits
- Validation: Sum of the first 9 digits, each multiplied by its position (1-9), modulo 11. The check digit can be 0-9 or 'X'.
- Sample: 0306406152 (Valid ISBN-10)

### ISBN-13 Number
- Length: 13 digits
- Validation: Alternating sum of the digits multiplied by 1 or 3, modulo 10.
- Sample: 9780306406157 (Valid ISBN-13)

### Universal Product Code (UPC)
- Length: 12 digits
- Validation: Sum of the odd-positioned digits (1-indexed), multiplied by 3, plus the sum of the even-positioned digits, modulo 10.
- Sample: 012345678905 (Valid UPC)

### Visa Credit Card Number
- Length: 16 digits
- Validation: Luhn algorithm
- Sample: 4111111111111111 (Valid Visa)

### MasterCard Number
- Length: 16 digits
- Validation: Luhn algorithm
- Sample: 5555555555554444 (Valid MasterCard)

### American Express (Amex) Card Number
- Length: 15 digits
- Validation: Luhn algorithm
- Sample: 378282246310005 (Valid Amex)

## Disclaimer: 
- This program aims to provide validation for various identification numbers using well-established algorithms and methods. However, it may not catch every possible requirement or edge case.
