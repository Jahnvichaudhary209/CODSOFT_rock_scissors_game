import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user, computer):
    
    if user == computer:
        return 'tie'
        
  
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissors' and computer == 'paper'):
        return 'user'
        

    return 'computer'

def main():
  
    print("  Welcome to Rock, Paper, Scissors!      ")
 
    print("Instructions: Type your choice each round.")
    print("Type 'exit' at any prompt to stop playing.\n")
    
  
    user_score = 0
    computer_score = 0
    round_num = 1
    
    while True:
        print(f"--- Round {round_num} ---")
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        
        
        if user_choice == 'exit':
            break
            
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input! Please check your spelling and try again.\n")
            continue
            
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
       
        result = determine_winner(user_choice, computer_choice)
        
        if result == 'tie':
            print("It's a tie match!")
        elif result == 'user':
            print("Nice! You won this round.")
            user_score += 1
        else:
            print("Bummer, the computer took this round.")
            computer_score += 1
            
     
        print(f"\nScoreboard -> You: {user_score} | Computer: {computer_score}")
        print("=====\n")
        
       
        play_again = input("Want to play another round? (y/n): ").strip().lower()
        if play_again != 'y' and play_again != 'yes':
            break
            
        round_num += 1

    print("\nThanks for playing!")
    print(f"Final Results -> Rounds Played: {round_num} | Final Score - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()
