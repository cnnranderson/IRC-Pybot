#-----Tic Tac Toe Protocol-----#
grid = [[' ',' ',' '],
		[' ',' ',' '],
		[' ',' ',' ']]

gameOver = True	
global p1
global p2
global turn
turn = False #false = p1, true = p2

def resetGrid():
	global gameOver
	global grid
	global turn
	turn = False
	gameOver = False
	grid = [[' ',' ',' '],
			[' ',' ',' '],
			[' ',' ',' ']]

def printGrid():
	sendMsg(" ----- ")
	for i in range(3):
		strout = '|'
		for j in range(3):
			strout += grid[i][j]
			strout += '|'
		sendMsg(strout)
	sendMsg(" ----- ")

def enterGame(player1,player2):
	sendMsg("Tic Tac Toe!")
	global p1
	global p2
	p1 = player1
	p2 = player2
	resetGrid()
	printGrid()

def place(x, y, player):
	global grid
	global turn
	global p1
	global p2
	if player == p1 and not turn:
		if grid[x][y] == ' ':
			grid[x][y] = "X"
			printGrid()
			turn = True
		else:
			sendMsg("Spot is already marked! Try a new coordinate.")
	elif player == p1 and turn:
		sendMsg("Sorry "+player+", it's not your turn!")
		
	if p2.find(player) != -1 and turn:
		if grid[x][y] == ' ':
			grid[x][y] = "O"
			printGrid()
			turn = False
		else:
			sendMsg("Spot is already marked! Try a new coordinate.")
	elif p2.find(player) != -1 and not turn:
		sendMsg("Sorry "+player+", it's not your turn!")