#!/usr/bin/python3
import math

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
	while True:
		choice = input("select a square, or q to exit ")
		if choice == 'q':
			return 'quit'
		elif choice.isdigit() == False:
			print("Please enter a number")
		elif int(choice) > max:
			print("Number out of range")
		else:
			return int(choice)

def record_choice(board, player, choice_coord):
	x = choice_coord[0]
	y = choice_coord[1]
	if player == 1:
		board[x][y] = 'X'
	elif player == 2:
		board[x][y] = 'O'
	return board

def num_to_coord(num, board):
	rows = len(board)
	columns = len(board[0])
	row_of_number = math.ceil(num/columns) - 1
	column_of_number = (num - row_of_number * columns) - 1
	result = [row_of_number, column_of_number]
	return result

def check_horizontal(board, rows = 3, columns = 3):
	for row in range(rows):
		score = 0
		for column in range(columns-1):
			if board[row][column] == board[row][column+1]:
				score +=1
			if score == columns - 1:
				print('horizontal win')
	
def check_vertical(board, rows = 3, columns = 3):
	for column in range(columns):
		score = 0
		for row in range(rows-1):
			if board[row][column] == board[row+1][column]:
				score +=1
			if score == rows - 1:
				print('vertical win')

def check_diag(board, rows = 3, columns = 3):
	score = 0
	for cell in range(columns-1):
		if board[cell][cell] == board[cell+1][cell+1]:
			score += 1
		if score == rows - 1:
			print('diagonal win')
	score_rl = 0
	for cell in range(rows-1):
		# check right to left
		if board[cell][-(cell+1)] == board[cell+1][-(cell+2)]:
			score_rl +=1
		if score_rl == rows - 1:
			print('diagonal win')
##Main loop##
board = make_board(HEIGHT, WIDTH)
player = 1
while True:
	print_board(board)
	choice = player_choice(board)
	if choice == 'quit':
		break
	#elif choice already has an X or O, print that
	#elif check if somebody has won, need function for that
	else:
		board = record_choice(board, player, num_to_coord(choice, board))
		check_vertical(board)
		check_horizontal(board)
		check_diag(board)
		if player == 1:
			player = 2
		else:
			player = 1
