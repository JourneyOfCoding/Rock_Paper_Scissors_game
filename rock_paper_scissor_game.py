import random  # Importing the random module for generating computer choices

def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors']
    
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()  # Getting user input and converting to lowercase
        
        if choice in valid_choices:  # Checking if the user's input is valid
            return choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])  # Returning a random choice for the computer

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You Win!"
    else:
        return "Computer Wins!"
    
def play_game():
    print("Let's play Rock Paper Scissors!")
    
    while True:  # Loop for playing multiple rounds
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        print(get_winner(user_choice, computer_choice))  # Printing the winner
        
        play_again = input("Do you want to play again? (Yes/No): ")
        
        while play_again.lower() not in ['yes', 'no']:
            play_again = input("Invalid choice. Please enter yes or no: ")
            
        if play_again.lower() == 'no':
            break
        
play_game()  # Starting the game
