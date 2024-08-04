import random
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def det_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif(user_choice == 'rock' and computer_choice == 'scissors') or\
         (user_choice == 'scissors' and computer_choice == 'paper') or\
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'
def game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = input("Please choose:(rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue
        computer_choice = get_computer_choice()
        print("Computer chose: ",computer_choice)
        result = det_winner(user_choice, computer_choice)
        if result == 'draw':
            print("It's a draw!")
        elif result == 'user':
            print("You Fabulous!")
            user_score += 1
        else:
            print("Don't give up!")
            computer_score += 1
        print("Score: You: ",user_score,"Computer: ",computer_score)
        play_again = input("Wanna play again?(yes/no): ").lower()
        if play_again != 'yes':
            break
    print("Thank you for playing!")
game()
