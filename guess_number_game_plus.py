import random
import sys

number = random.randint(1, 100)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("choose a difficulty level: 'easy' or 'hard': ")

while True:
    if difficulty.lower() == 'easy':
        max_attempts = 10
        break
    elif difficulty.lower() == 'hard':
        max_attempts = 5
        break
    else:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
        difficulty = input("choose a difficulty level: 'easy' or 'hard': ")
        
attempts = 0
while attempts < max_attempts:
    guess = input("Guess a number between 1 and 100: ")
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if guess < 1 or guess > 100:
        print("Please guess a number within the range of 1 to 100.")
        continue
    
    attempts += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number} correctly in {attempts} attempts.")

        if attempts == 1:
           print("评价:给到夯")
        
        if attempts <= 3:
            print("评价:给到牛逼")
            
        if attempts <= 5:
            print("评价:给到666")
            
        if attempts >5:
            print("评价:拉完了")
        break
    
else:
    print(f"Sorry, you've run out of attempts. The number was {number}.")
sys.exit()


























