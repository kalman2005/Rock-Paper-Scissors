import random

def combat():
    global playerHealth, opponentHealth, playerMove, opponentMove, streak, rockStreak, paperStreak, scissorsStreak, endgame, winner, loser

    if endgame == True:
        if winner == True:
            print("You've won!!! congratulations")
            quit
            exit
        if loser == True:
            print("You've lost!")
            quit
            exit

    else:
        # if the player move is rock activate this script
        if playerMove == rock:
            rockStreak += 1
            paperStreak = 0
            scissorsStreak = 0
            streak = rockStreak + paperStreak + scissorsStreak
            print("\nYou're opponent picked", opponentMove)
            if opponentMove == 'rock':
                print("You've tied")
                playerMove = None
                print("\nYou have", playerHealth, "health left!")
                print("You're opponent have", opponentHealth, "health left!")
                playerMove = input('\nRock, Paper, Scissors? \n:')
                    
            if opponentMove == 'paper':
                print("You've lost")
                playerHealth -= 5
                playerMove = None
                print("\nYou have", playerHealth, "health left!")
                print("You're opponent have", opponentHealth, "health left!")
                playerMove = input('\nRock, Paper, Scissors? \n:')

            if opponentMove == 'scissors':
                print("You've won")
                opponentHealth -= 5
                playerMove = None
                print("\nYou have", playerHealth, "health left!")
                print("You're opponent have", opponentHealth, "health left!")
                playerMove = input('\nRock, Paper, Scissors? \n:')

        # if the player move is paper activate this script
        if playerMove == paper:
            rockStreak = 0
            paperStreak += 1
            scissorsStreak = 0
            streak = rockStreak + paperStreak + scissorsStreak
            print("\nYou're opponent picked", opponentMove)
            if opponentMove == 'rock':
                print("You've won")
                opponentHealth -= 5
                playerMove = None
                playerMove = input('\nRock, Paper, Scissors? \n:')
            if opponentMove == 'paper':
                print("You've tied")
                playerMove = None
                playerMove = input('\nRock, Paper, Scissors? \n:')
            if opponentMove == 'scissors':
                print("You've lost")
                playerHealth -= 5
                playerMove = None
                playerMove = input('\nRock, Paper, Scissors? \n:')

        # if the player move is scissors activate this script
        if playerMove == scissors:
            rockStreak = 0
            paperStreak = 0
            scissorsStreak += 1
            streak = rockStreak + paperStreak + scissorsStreak
            print("\nYou're opponent picked", opponentMove)
            if opponentMove == 'rock':
                print("You've lost")
                playerHealth -= 5
                playerMove = None
                playerMove = input('\nRock, Paper, Scissors? \n:')
            if opponentMove == 'paper':
                print("You've won")
                opponentHealth -= 5
                playerMove = None
                playerMove = input('\nRock, Paper, Scissors? \n:')
            if opponentMove == 'scissors':
                print("You've tied")
                playerMove = None
                playerMove = input('\nRock, Paper, Scissors? \n:')
        

# starting health
playerHealth = 20
opponentHealth = 20

# start moves
playerMove = input('Rock, Paper, Scissors? \n:')
opponentMove = random.choice(['rock', 'paper', 'scissors'])

# the different moves
# left is what the code calls it
# right is what the player needs to input
rock = 'Rock'
paper = 'Paper'
scissors ='Scissors'

endgame = False
winner = False
loser = False

rockStreak = 0
paperStreak = 0
scissorsStreak = 0
streak = 0

# activating every function in the while true loop
while True:
    combat()
    
    # checks if either party should be dead or not
    if playerHealth == 0:
        winner = True
        endgame = True
    if opponentHealth == 0:
        loser = True
        endgame = True
    
    if streak <= 2:
        opponentMove = random.choice(['rock', 'paper', 'scissors'])
    if rockStreak > 2:
        opponentMove = random.choice(['paper'])
    if paperStreak > 2:
        opponentMove = random.choice(['scissors'])
    if scissorsStreak > 2:
        opponentMove = random.choice(['rock'])
