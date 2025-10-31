Number Guessing Game (Python) – README



Overview


This is a Python-based Number Guessing Game designed as part of a learning project to practice programming logic, loops, input validation, and Git version control workflow.
The game generates a random number between 1 and 100, and the player has 7 attempts to guess it correctly. After each round, the player can choose to replay. The program also tracks statistics such as total games played, wins, losses, and average score across sessions.


Requirements


System requirements

•	Any operating system that supports Python (Windows, macOS, Linux)

•	Internet access (only needed for GitHub cloning or downloading)

Software requirements

•	Python 3.8 or later

•	A code editor or IDE (such as VS Code, PyCharm, or IDLE)


Features


•	Random number generation between 1–100 

•	Input validation to handle invalid or out-of-range guesses

•	A maximum of 7 attempts per round

•	Score system based on number of attempts used

•	Replay option to play multiple rounds

•	Statistics tracking:

  o	Total games played

  o	Total wins

  o	Total losses

  o	Average score


How the game works


1.	When the game starts, it welcomes the player and generates a random number.

2.	The player must guess a number between 1 and 100.

3.	The game gives hints such as “Too high” or “Too low”.

4.	The player gets 7 chances to guess correctly.

5.	If guessed correctly:

a.	The game calculates a score (higher if fewer attempts are used).

6.	If all attempts are used:

a.	The game reveals the correct number.

7.	After each game, the player is asked if they’d like to play again.

8.	When the player exits, the program shows their statistics summary.


Setup instructions


1.	Clone the Repository

To get a local copy of this project, open your terminal and run:
git clone https://github.com/Luqman2306/rockborne_number_guessing_game.git

Then move into project directory:
cd rockborne_number_guessing_game

2.	Check Python is installed


3.	Run the Game 

In your terminal, run:
python number_guessing_game.py

You should see:

Welcome to the Number Guessing Game

I'm thinking of a number between 1 and 100.

You have 7 attempts to guess it correctly.



Key functions

Function	Purpose

get_valid_guess()	Ensures the player enters a valid number between 1–100


play_game()

	Runs one round of the game (tracks attempts and score)


show_statistics()

	Displays all-time stats: total games, wins, losses, average score


main()

	Controls replay and when to show statistics

