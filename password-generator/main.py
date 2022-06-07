import random
from characters import letters, numbers, symbols

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Ordered - not randomised:
password=""
for l in range(1,nr_letters+1):
  random_letter=random.choice(letters)
  password+=random_letter

for s in range(1,nr_symbols+1):
  random_symbol=random.choice(symbols)
  password+=random_symbol

for n in range(1,nr_numbers+1):
  random_number=random.choice(numbers)
  password+=random_number

print(f'Your password is : {password}')

#Hard Level - Order of characters randomised:

password_list=[]
for l in range(1,nr_letters+1):
  random_letter=random.choice(letters)
  password_list.append(random_letter)

for s in range(1,nr_symbols+1):
  random_symbol=random.choice(symbols)
  password_list.append(random_symbol)

for n in range(1,nr_numbers+1):
  random_number=random.choice(numbers)
  password_list.append(random_number)

random_pass=random.shuffle(password_list)

password_random=""
for i in password_list:
  password_random+=i
print(f'Your password is : {password_random}')

quit=input("Press 'q' to quit: ").lower()
if quit=='q':
  exit()
