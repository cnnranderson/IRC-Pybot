import socket
import sys
import datetime
import time
import random

import tictactoe

#------------------------Bot Socket Connect-----------------------#
server = "irc.freenode.net"       #settings
channel = "#conner"
botnick = "Samich-bot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                     #defines the socket
print "connecting to: "+server
irc.connect((server, 6667))                                                 #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :A simple bot!!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                                            #sets nick
irc.send("PRIVMSG nickserv :identify target\r\n")                           #auth

time.sleep(3)

irc.send("JOIN "+ channel +"\n")   #join the channel
#-----------------------------------------------------------------#


#--IRC Commands--#
def sendMsg(message):
	irc.send('PRIVMSG '+channel+' :' + message + '\r\n')
	
def disconnect():
	irc.shutdown(2)
	irc.disconnect()
	irc.close()

def getUser(message):
	parse = message.split('!')
	return parse[0].strip(':')

def parseMessage(message):
	count = 0
	txt = 0
	for i, value in enumerate(message):
		if value == ':':
			count += 1
		if count == 2:
			txt = i+1
			break
	return message[txt:]
#---------------#


#--------------------------Bot Functions--------------------------#
def flipCoin(): #Flips a coin
	coin = random.randint(0,1)
	if coin == 0: 
		strout = "Heads"
	else:
		strout = "Tails"
	irc.send('PRIVMSG '+channel+' :Coin flip resulted in '+strout+'!\r\n')

def sayHello():
	sendMsg("Hello everyone :D")

def makeSandwich():
	sendMsg("k")
	sendMsg(" ")
	sendMsg(" ,,,,,,,,")
	sendMsg("{--------}")
	sendMsg("~~~~~~~~~~")
	sendMsg("==========")
	sendMsg("@@@@@@@@@@")
	sendMsg("{--------}")
	sendMsg(" ''''''''")

#-----------------------------------------------------------------#



#----------------------------Bot Loop-----------------------------#
while 1:    #puts it in a loop
	text=irc.recv(2040) #receive the text

	if text.find('PING') != -1:
		irc.send('PONG ' + text.split() [1] + '\r\n')
		
	user = getUser(text)
	text = parseMessage(text)
	#print user+': '+text
	
	if text.find('!reload') != -1:
		reload(tictactoe)
	
	if user == 'samich':
		if text.find('!flip') != -1:
			flipCoin()
		if text.find('!dc') != -1:
			disconnect()
		if text.find('!ttt') != -1 and tictactoe.gameOver:
			tictactoe.enterGame(user,'null')
		if text.find('Say hello bot!') != -1:
			sayHello()
	
	if text.find('make me a sammich') != -1:
		makeSandwich()
		
	#-------Tic Tac Toe Commands----------#
	if not tictactoe.gameOver:
		if text.startswith("-ttt/help"):
			sendMsg("Commands:")
			sendMsg("-whoplay : shows who is currently playing.")
			sendMsg("-playwith : player one can specify a user to play with.")
			sendMsg("-set (Letter)(Number) : eg. -set A1, sets player piece on grid.")
			sendMsg("-endgame : player one can choose to kill the game.")
		if text.startswith("-whoplay"):
			sendMsg("Current Users Playing: " + tictactoe.p1 + ", " + tictactoe.p2)
		if text.startswith("-playwith") and tictactoe.p1 == user:
			tictactoe.p2 = text.split(" ")[1]
			sendMsg("Now playing Tic Tac Toe with: "+tictactoe.p2)
		if text.startswith("-endgame") and tictactoe.p1 == user:
			tictactoe.resetGrid()
			sendMsg("Game Ended.")
		if text.startswith("-set "):
			text = text[5:]
			if text.startswith("A"):
				if isinstance(int(text[1]), int):
					num = int(text[1])
					if num < 4 and num > 0:
						tictactoe.place(0,num-1,user)
			if text.startswith("B"):
				if isinstance(int(text[1]), int):
					num = int(text[1])
					if num < 4 and num > 0:
						tictactoe.place(1,num-1,user)
			if text.startswith("C"):
				if isinstance(int(text[1]), int):
					num = int(text[1])
					if num < 4 and num > 0:
						tictactoe.place(2,num-1,user)
					
#-----------------------------------------------------------------#