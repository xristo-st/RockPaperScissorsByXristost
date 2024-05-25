from random import randint

moves = ('rock', 'paper', 'scissors')
moves_keys = 'rps'
player_move = input("Choose [r]ock, [p]aper or [s]cissors: ").lower()
if player_move not in moves_keys:
    print("Invalid choice! Exiting...")
    exit(1)
player_move = moves_keys.index(player_move) # number from 0 to 2
print(f"Your move is: {moves[player_move]}")
computer_move = randint(0,2) # random number from 0 to 2
print(f"Computer move is: {moves[computer_move]}")
sub = player_move - computer_move
if sub == 0:
    print("The result is draw.") # two moves are equal
elif sub == 1 or sub == -2:
    print("You win!")
else:
    print("The computer win!")
