import random
from game_data import data
from art import logo,vs

def random_choice():
  account_b=random.choice(data)
  return account_b
# Format account data into printable format.
def format_data(acc):
  '''format data into printable format'''
  account_name=acc["name"]
  account_descr=acc["description"]
  account_country=acc["country"]
  return(f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess,a_follow,b_follow):
  '''Check if user is correct.'''
  if a_follow>b_follow:
    return guess=="a"
  else:
    return guess=="b"

# Generate a random account from the game data.
def game():
  print(logo)
  score =0
  game_end=False
  
  while not game_end:
    account_b=random_choice()
    account_a=random.choice(data)
  
    while account_a==account_b:
      account_b=random.choice(data)
    print('*'*50)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    
    # Ask user for a guess.
    guess=input("Who has more followers?Type 'A' or 'B': ").lower()
    
    # Check if user is correct.

    a_follower=account_a["follower_count"]
    b_follower=account_b["follower_count"]

    is_correct=check_answer(guess,a_follower,b_follower)
    
    # Feedback  and Score Keeping.
    if is_correct:
      score+=1
      print(f"You're right! Current score: {score}")
 
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_end=True

game()
