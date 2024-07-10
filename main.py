import random

print("Welcome to the number guessing game.")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 101)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")

if(difficulty == 'easy'):
  guesses = 10
elif(difficulty == 'hard'):
  guesses = 5
  
print(f'You have {guesses} guesses to get the correct number.')

while(guesses > 0):
  guess = int(input("Make a guess:\n"))
  if(guess == number):
    print("You guessed correct. The number was {number}")
    break
  else:
    guesses -= 1
    if(guess > number):
      print(f"You guessed too high. You have {guesses} guesses left.")
    else:
      print(f"You guessed low high. You have {guesses} guesses left.")
if(guess == 0):
  print(f"You ran out of guesses. The number was {number}. Game Over.")