global player
temp=0

print("Tic Tac Toe by Abhisek\n")
#board------------------------------
board=["-","-","-",
	   "-","-","-",
	   "-","-","-"]

#display the board---------------------------
def display():
	print(board[0]+"|"+board[1]+"|"+board[2])
	print(board[3]+"|"+board[4]+"|"+board[5])
	print(board[6]+"|"+board[7]+"|"+board[8])
#---------------------------------------------
display()
winner=None
still_running=True
def play():
	taking_input()
	#changed_display()
	check_winner()
	display()
	if still_running:
		play()
	else:
		print_winner()

#----------------------------------
#change player--------------
global z
z=0
def change_player():
	global change_player
	global player
	global z
	
	#print(z)
	if z%2==0:
		player='X'
	else:
		player='O'
	z+=1
#taking input-----------------

global taking_input
def taking_input():
	global player
	global a
	a=int(input("Enter the no between 1-9\n"))
	check_range()
	
	if board[a-1]=='-':
		change_player()
		board[a-1]=player
		#change_player()
	else:
		print("Number is already taken try something else\n")
		taking_input()
	

#check range--------------------
def check_range():
		global a
		if a not in range(1,10):
			print("Not in range try again\n")
			a=int(input("Enter the no between 1-9\n"))
			check_range()
#changed display--------------


	



#check_winner--------------------
def check_winner():
	check_row()
	check_col()
	check_dia()
	check_tie()

#-------------------------row---------

def check_row():
	p=board[0]==board[1]==board[2]!='-'
	q=board[3]==board[4]==board[5]!='-'
	r=board[6]==board[7]==board[8]!='-'
	
	global still_running
	if (p or q or r ):
		still_running=False
		


#------------------------col---------

def check_col():
	p=board[0]==board[3]==board[6]!='-'
	q=board[1]==board[4]==board[7]!='-'
	r=board[2]==board[5]==board[8]!='-'
	global still_running
	if p or q or r :
		still_running=False
#------------------------dia------------

def check_dia():
	p=board[0]==board[4]==board[8]!='-'
	q=board[2]==board[4]==board[6]!='-'
	global still_running
	if p or q :
		still_running=False
#==================print tie

def check_tie():
	global still_running
	global temp
	if '-' not in board:
		if still_running :
			#global still_running
			still_running=False
			global temp
			temp=10
			#print("The game is Tie")
			

def print_winner():
	global temp
	if temp==10:
		print("The game is tie\n\n")
		play_again()
	else:
		if z%2==0:
			print("O won\n\n")
			play_again()
		else:
			print("X won\n\n")
			play_again()

def play_again():

	q=int(input("Want to play again  1/0 ?\n"))
	#print(q)
	if q==1:
		global temp
		global still_running
		global z
		temp=0
		z=0
		still_running=True
		for i in range(0,9):
			board[i]="-"
		display()
		play()
	else:
		print("Thank You\n\n")



play()








