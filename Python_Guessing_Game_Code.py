import random # import the random module to generate random numbers

# Global counters to track statistics across multiple games
total_games = 0
total_wins = 0
total_losses = 0
total_score = 0

def get_valid_guess():
    """Ask the user to enter a number between 1 and 100. Keeps asking until a valid integer is entered."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100):"))
            # Check that the number is within the valid range 
            if 1 <= guess <=100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            # Handles any non-numeric input to prevent program crashes 
            print("Invalid input. Please enter a number!")

def play_game():
    """
    This function runs a single round of the guessing game. 
    It compares the player's guesses with the randomly chosen number 
    and gives feedback after each attempt.
    """
    global total_games, total_wins, total_losses, total_score

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1,100)
    attempts_allowed = 7
    attempts_used = 0
    total_games += 1  # Count this game

    print("\nI'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it correctly")

    # Main guessing loop
    while attempts_used < attempts_allowed:
        guess = get_valid_guess()
        attempts_used += 1

        if guess == number_to_guess:
            print(f"Correct! You guessed it in {attempts_used} attempts.")
            # The fewer attempts used, the higher the score 
            score = max(0, 100 - (attempts_used - 1) * 10)
            total_score += score
            total_wins += 1
            print(f"Your score for this round: {score}")
            break
        elif guess < number_to_guess:
            print("Too low. Try again")
        else: 
            print("Too high. Try again!")
    else:
        # This will run if the player runs out of attempts
        print(f"Out of attempts! The correct number was {number_to_guess}.")
        total_losses += 1


def show_statistics():
    """
    Displays overall player statistics after all games are finished.
    Includes total games, wins, losses, and average score.
    """
    print("n\Game Statistics:")
    print(f"Total Games Played: {total_games}")
    print(f"Games Won: {total_wins}")
    print(f"Games Lost: {total_losses}")
    if total_games > 0:
        average_score = total_score / total_games
        print(f"Average Score: {average_score:.2f}")
    print("Thanks for playing!")


def main():
    """
    Controls the overall game flow. 
    Allows the player to play multiple rounds and choose when to quit.
    """
    print("Welcome to the Number Guessing Game")

    while True:
        play_game() # Run one round of the game 
        replay = input("\nWould you like to play again? (y/n): ").strip().lower()
        if replay != "y":
            # If the player chooses not to continue, show their stats
            show_statistics()
            break


# This ensures the game only runs when this file is executed directly
if __name__ == "__main__":
    main()
