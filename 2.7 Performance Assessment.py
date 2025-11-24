# My Name: Ishmael Bennett
# Date Today: November 23, 2025
# What this program does: It plays a number guessing game and then shows how loops work.

# --- Setting up our containers (variables) ---
studentIdInput = ""
userNameInput = ""
secretNumber = 5  # This is the number the user needs to guess
userGuessAttempt = 0
howManyGuesses = 0
keepPlayingGame = True

# --- Asking the user for info ---
userNameInput = input("What is your name? ")
studentIdInput = input("What is your studentID? ")

# --- The Guessing Game Part ---
# We keep asking until they get it right
while keepPlayingGame:
    try:
        # Ask for their guess and turn it into a whole number
        userGuessAttempt = int(input("Please guess a number between 1 and 10..."))
        howManyGuesses += 1 # Add one to our guess counter

        # Check if their guess is too low, too high, or just right
        if userGuessAttempt < secretNumber:
            print("You guessed too low")
        elif userGuessAttempt > secretNumber:
            print("You guessed too high")
        else: # This means userGuessAttempt is equal to secretNumber
            print(f"Congratulations, {userNameInput}! You guessed the number in {howManyGuesses} tries!")
            keepPlayingGame = False # Stop the game, they got it!
    except ValueError:
        # If they type something that's not a number, tell them
        print("Invalid input. Please enter a whole number.")

# --- The 'while' loop show-and-tell ---
print("\nOutput from the 'while' loop:")
currentNumberInWhile = secretNumber # Start with the secret number (e.g., 5)
loopCounterWhile = 0 # This helps us count how many times the loop runs

# We want this loop to run 5 times
while loopCounterWhile < 5:
    loopCounterWhile += 1 # Make our counter go up by one each time
    # Add 1 to currentNumberInWhile
    currentNumberInWhile += 1
    # Show what happened
    print(f"{secretNumber} incremented by {loopCounterWhile} is {currentNumberInWhile}")

# --- The 'for' loop show-and-tell (does the same as the while loop) ---
print("\nOutput from the 'for' loop:")
startNumberFor = secretNumber # Start again with the secret number (e.g., 5)

# This loop also runs 5 times (i will be 0, 1, 2, 3, 4)
for i in range(5):
    # Calculate the new number. We use (i + 1) because i starts from 0,
    # but we want to show 'incremented by 1', 'incremented by 2', etc.
    newNumberInFor = startNumberFor + (i + 1)

    # Show what happened
    print(f"{secretNumber} incremented by {i + 1} is {newNumberInFor}")
