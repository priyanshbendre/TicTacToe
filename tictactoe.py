# Tic-Tac-Toe implementation

def draw_board(theboard):
	vertical_divider = "---+---+---"
	horizontal_divider = "   |   |"
	print(" {} | {} | {} ".format(theboard[0],theboard[1],theboard[2]))
	print(vertical_divider)
	print(" {} | {} | {} ".format(theboard[3],theboard[4],theboard[5]))
	print(vertical_divider)
	print(" {} | {} | {} ".format(theboard[6],theboard[7],theboard[8]))
	print("")

#To Alternate between Users
def switch_user(current_user):
	if current_user == True:
		return False
	return True

def evaluate(winner,theboard):
	if ((theboard[0]==theboard[1]==theboard[2]) or (theboard[3]==theboard[4]==theboard[5]) or (theboard[6]==theboard[7]==theboard[8])
	or (theboard[0]==theboard[3]==theboard[6]) or (theboard[1]==theboard[4]==theboard[7]) or (theboard[2]==theboard[5]==theboard[8])
	or ((theboard[0]==theboard[4]==theboard[8])) or (theboard[2]==theboard[4]==theboard[6])):
		winner = True
	return winner	

def user_input(theboard, current_user):
	user_in = int(input("Enter board location: "))
	if str(theboard[user_in]).isalpha():
		print("Please enter different block number!")
		user_input(theboard,current_user)
	else:
		if current_user:
			theboard[user_in] = 'X'
		else:
			theboard[user_in] = 'O'
		draw_board(theboard)
		current_user = switch_user(current_user)
	return current_user

# def gitplay(theboard):
# 	gamestate = open("gitgame.txt")
# 	gamestate.write(theboard)

	
#Main Function
if __name__ == '__main__':
	theboard = [0,1,2,3,4,5,6,7,8]
	winner = False
	current_user = True
	draw_board(theboard)
	print ("1st Player is 'X' and 2nd Player is 'O'!")

	test_while_count = 0
	while test_while_count<9 :
		current_user = user_input(theboard,current_user)
		winner = evaluate(winner,theboard)
		if winner:
			if current_user:
				print("Player 2 is the Winner!") #because its player 1's turn therefore the status is player 1
			else:
				print("Player 1 is the Winner!")
			print("\033[1;32;40m Winner!")
			break;
		test_while_count+=1
	#gitplay(theboard)
