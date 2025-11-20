# Mini Project – Countdown Timer (with 1-second gap)
# Goal:
# Print a countdown before something “exciting” happens (like “Launching...” or
# “Happy New Year!”).
import time
count = int(input("Enter a counter number: "))
print("CountDown start now >>>")
for i in range(count, 0, -1):
  print(i)
  time.sleep(1)
print("Happy New Year!")  

# Mini Project – Multiplication Table
# Goal: Print the multiplication table of a number using a loop.
num = int(input("Enter a number for multiplication: "))
for i in range(1,11):
  print(num*i)
  
# Mini Project – Guess the Number Game
import random
rightGuess = random.randint(1,10)
guessNum = int(input("Enter guessing number: "))
while(1):
  if guessNum!=rightGuess:
    print("Wrong guess! Try again.")
    guessNum = int(input("Guess again: "))
  elif guessNum==rightGuess:
    print("Congratulations, Khushboo! You guessed it right 🎉")
    break
  