from random import randrange

## 1---->O 先手
## 2---->X 后手

def display(board):     			## print the current state of the game
	print('\nNow Displaying the board:')
	print(' ',' 1 2 3')
	for i in range(3):
		print(i+1,' ',end='')
		for j in range(i*3,i*3+3):
			if board[j]==0:
				print('- ',end='')
			elif board[j]==1:
				print('O ',end='')
			else:
				print('X ',end='')
		print('')
	print('')


def checkwin(board):				##check if anyone wins the game
	## 'board' is the current board to check win
	# check row
	for i in range(0,8,3):
		if(board[i]==board[i+1] and board[i]==board[i+2] and board[i] != 0):
			return board[i]

	# check column
	for i in range(3):
		if(board[i]==board[i+3] and board[i]==board[i+6] and board[i] != 0):
			return board[i]

	# check diagnal
		# \\\\\\
	if board[0] == board[4] and board[0] == board[8] and board[0] != 0 :
		return board[0]
		# //////
	if board[2] == board[4] and board[2] == board[6] and board[2] != 0:   
		return board[2]
	return 0


def player_choice():				## player choose to take position
	while True:
		player = input('If you want Offensive Position, enter \'1\', else enter \'2\'\n')
		if player.isdigit() != True or ():
			print('Please Re-Make Valid Decision')
			continue
		player = int(player)
		if (player != 1 and player != 2):
			print('Please Re-Make Valid Decision')
			continue
		else:
			return player


def player_move():					## player do their move
	while True:
		move = input('Please decide your move[1-9]: ')
		if move.isdigit() != True:
			print('Please make valid move')
			continue
		move = int(move)
		if move>9 or move<1:
			print('Please re-decide your move between 1 and 9')
		else:
			return move-1


def cpt_move(board, sim, player, computer):			## computer decides its move
    ## 'board' is the current board to make next move
	## 'sim' is the number of simulation to do every step
	## 'player' is player's position
	## 'computer' is computer's position
	current = []
	move = []
	last_move = [player,computer]

	for i in range(9):
		if board[i]==0:
			move.append(i)
	for each in move:   			## for each legal move
		win = 0

		for j in range(sim):     	## simulate N times
			move_record = 1
			arr = board.copy()
			arr[each] = last_move[move_record%2]
			move_record += 1
			new_move = move.copy()
			new_move.remove(each)
			while new_move:     	## randomly make moves
				empty = new_move[randrange(len(new_move))]
				arr[empty] = last_move[move_record%2]
				move_record += 1
				new_move.remove(empty)
				result = checkwin(arr)    ## check who wins after each move
				# print('checkwin result:', result)
				if result == computer:
					# print('win add is:', 10-(sum(x > 0 for x in arr)))
					win += (10-(sum(x > 0 for x in arr)))*10
					break
				elif result == player:
					# print('win minus is:', 10-(sum(x > 0 for x in arr)))
					win -= (10-(sum(x > 0 for x in arr)))*10
					break
			if (0 not in new_move):
				result = checkwin(arr)
				if result == 0:
					win += 50
		current.append(win)
	print(current)
	return move[current.index(max(current))]


def winner_check(winner, player, computer):	## check who wins the game
	## 'board' is the current board to check who's winner
	## 'player' is the position of player plays
	## 'computer' is the position of computer plays
	if winner == 0:
		print('Draw!')
	elif winner == player:
		print('Player Wins!')
	else:
		print('Computer Wins!')




def main():
	board = [0 for i in range (9)]
	print('*'*40, '\nWelcome to Our Tic-Toc-Toe Game!')
	print('*'*40)
	print('Here is the board position check table for you :\n1 2 3\n4 5 6\n7 8 9\n')
	print('Now Please Decide to Take Offensive Position(O) or Deffensive Position(X)')
	computer = 1
	player = player_choice()

	if player == 1:
		computer = 2
		move = player_move()
		board[move] = player
		display(board)

	while (0 in board):
		move = cpt_move(board, 2000, player, computer)
		# print(board, player, computer)
		board[move] = computer
		print('Computer take move:', move+1)
		display(board)
		if checkwin(board)!=0 :
			winner_check(checkwin(board),player, computer)
			break

		if (0 in board):
			while True:
				move = player_move()
				if board[move]!= 0:
					print('Position Already Been Occupied!')
				else:
					break
			board[move] = player
			display(board)
			result = checkwin(board)
			if result!=0 :
				winner_check(checkwin(board), player, computer)
				break
	if (0 not in board):
		winner_check(checkwin(board),player, computer)
	return


	# print(player)

	# print('check display')
	# display(board)
	# print('display done!')

	# print('check move')
	# move = player_move()
	# board[move] = 2
	# display(board)
	# print('move done!')

	# board[0] = 1
	# board[4] = 1
	# board[8] = 1

	# print('check checkwin')
	# print(checkwin(board))
	# print(display(board))
	# print('check win done!')

if __name__ == '__main__':
	main()





















