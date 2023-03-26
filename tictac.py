#!/usr/bin/python3

HEIGHT = 3
WIDTH = 3

def make_board(width, height):
	board = []
	i = 1
	for x in range(height):
		board.append([]) # make (width) number of rows
		for y in range(width):
			board[x].append([i]) # make (height) number of columns 
			i += 1
	return board

def print_board(board):
	for row in board:
		print(row)

def player_choice(board):
	#ask for input and return an int within board range
	max = len(board) * len(board[0])
	choice = input("select a square")
	if choice.isdigit() == False:
		print("Please enter a number")
	elif int(choice) > max:
		print("Number out of range")
	else:
		return int(choice)

def record_choice(board, player, choice):
	if player == 1:
		board[0][choice] = 'X'
	return board
	

board = make_board(HEIGHT, WIDTH)
print_board(board)
board = record_choice(board, 1, player_choice(board))
print_board(board)

