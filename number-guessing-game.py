import sys

class NumberGuessingGame:

    def __init__(self):
        self.welcome_message()
        self.player = ""
        self.score = 0

    def welcome_message(self):
        print('''
            Welcome to the Number Guessing Game!

            HOW TO PLAY
            You are required to guess the hidden number.
            These numbers are of whole numbers.

            There are three difficulty levels in the game:
            EASY LEVEL - you get 6 guesses of numbers between 1 and 10.
            MWDIUM LEVEL - you get 4 guesses of numbers between 1 and 20.
            HARD LEVEL - you get 3 guesses of numbers between 1 and 50.

            Good luck!
            ''')

    def set_game(self):
        # The game levels keys and requirements in a dictionary
        gameLevels = {
            1: {'level':'easy', 'tries':6, 'max_num':10},
            2: {'level':'medium', 'tries':4, 'max_num':20},
            3: {'level':'hard', 'tries':3, 'max_num':50}
        }
        # Set the player's name
        self.player = input("Enter yout name: ")
        # Set the game difficulty level and the level requirements
        try:
            choice_level_key = int(
                input("Choose a difficulty level.\n1 for EASY, 2 for MEDIUM, 3 for HARD. Your Choice: ")
            )
        except ValueError: print("Oops! Not a valid key.")
        else:
            if (choice_level_key in gameLevels.keys()):
                level = gameLevels[choice_level_key]
                print(f"The game difficulty level has been set to {level['level']}.")
            else :
                print("Oops! Not a valid key for a difficulty levels.")
                sys.exit()
        return gameLevels[choice_level_key]['tries'], gameLevels[choice_level_key]['max_num']

    def start_game(self, given_tries, max_number_range):
        import random
        print(f"\nA number has been generated from 1 - {max_number_range} range. What is your guess?")
        tries = given_tries
        setNumber = random.randrange(1, max_number_range+1)
        while (tries > 0):
            try: guessFromPlayer = int( input("Your guess: ") )
            except ValueError: print("Wrong input! You're lucky. It won't count.")
            else:
                if (setNumber == guessFromPlayer):
                    self.score += 1
                    print("Ooin! You're doing well. On to the next one.")
                    self.start_game(tries, 3)
                else:
                    tries = tries - 1
                    if (tries > 0): print(f"Wrong! Now, you have {tries} tries left. Try again.")
                    else: print(f"\nSorry, {self.player}. No more tries.\nGame over!\n")
        print(f"At the end of the game, player {self.player} scored {self.score} points...")
        sys.exit()

def main():
    newGame = NumberGuessingGame()
    tries, max_number = newGame.set_game()
    newGame.start_game(tries, max_number)

main()
