#!/usr/bin/python3

HEIGHT = 5
WIDTH = 6

def make_board(width, height):
	board = []
	i = 1
	for x in range(height):
		board.append([]) # make (width) number of rows
		for y in range(width):
			board[x].append([i]) # make (height) number of columns 
			i += 1
	return board

a = make_board(HEIGHT, WIDTH)
print(a)
print(a[0])
print(a[0][2])

