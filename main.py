# Import necessary modules
from random import randint  # To generate a random number for the game
from replit import clear    # To clear the screen between rounds for better user experience

# List of invalid characters that can't be guessed (though it's not directly used in the game)
invalid_carc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', '"', "'", '<', ',', '>', '.', '?', '/', '`', '~']
guess_hist = []  # To track previously guessed numbers, so the user doesn't repeat them

# Function to ask the user if they want to play again
def tryagain():
  try_yn = input("Would you like to try again? 'y' or 'n'")  # Prompt for a retry
  if try_yn == "y":  # If user wants to play again
    clear()  # Clears the screen for a fresh start
    game()  # Calls the game function again to restart
  elif try_yn == "n":  # If user doesn't want to play again
    print("Goodbye.")  # Prints a farewell message

# Main game function
def game():
  number = randint(1, 100)  # Generate a random number between 1 and 100
  num_atempts = 0  # Initialize the number of attempts
  print("Welcome to the Number Guessing Game!")  # Game greeting
  dif = input("Would you like to play on 'easy' or 'hard'?")  # Ask user for difficulty
  if dif == "easy":  # If user selects easy difficulty
    num_atempts = 9  # Set number of attempts for easy
  elif dif == "hard":  # If user selects hard difficulty
    num_atempts = 4  # Set number of attempts for hard
  print(f"You have {num_atempts +1} attempts to guess the number.")  # Display attempts
  print("I'm thinking of a number between 1 and 100.")  # Hint to the user about the range

  # User makes the first guess
  guess = int(input("Guess a number between 1 and 100:"))

  # Main game loop to handle guessing
  while guess != number:  # Continue until the guess is correct
    if guess in guess_hist:  # Check if the user already guessed the number
      print("You already guessed the number!")
    elif guess > 100 or guess < 1:  # Check if the guess is out of the valid range
      print("You have entered an invalid number.")
    elif guess < number:  # If the guess is too low
      print("Too low.")
      num_atempts -= 1  # Decrease the number of remaining attempts
      guess_hist.append(guess)  # Add guess to the history
    else:  # If the guess is too high
      print("Too high.")
      num_atempts -= 1  # Decrease the number of remaining attempts
      guess_hist.append(guess)  # Add guess to the history
    print(f"You have {num_atempts +1} attempts left.")  # Show remaining attempts
    guess = int(input("Guess again:"))  # Prompt for the next guess

    # Check if the user has exhausted all attempts
    if num_atempts == 0:
      print("You lose.")  # If no attempts remain, the user loses
      tryagain()  # Ask the user if they want to try again

  # If the user guesses the number correctly
  if guess == number:
    print("You win!")  # Congratulate the user
    tryagain()  # Ask the user if they want to try again

# Start the game
game()
