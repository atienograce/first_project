from random import randint

choices = ['rock', 'paper', 'scissors']

while True:
    computer = choices[randint(0,2)]
    player = input("rock, paper or scissors? (or end the game) ")
    if player == 'end the game':
        print("The game has ended")
        break
    elif player == computer:
        print("Tie!")
    elif player == 'rock':
        if computer == 'paper':
            print(f"You lose!{computer} beats {player}")
        else:
            print(f"You win!{player} beats {computer} ")
    elif player == 'paper': 
        if computer == "scissors":
            print(f"You lose!{computer} beats {player}")
        else:
            print(f"You win!{player} beats {computer}")  
    elif player == 'scissors':
        if computer == 'rock':
            print(f'You lose!{computer} beats {player}')
        else:
            print(f"You win!{player} beats {computer}")
    else:
        print("Check your spelling...")
 
