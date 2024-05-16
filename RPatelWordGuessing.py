import random
import matplotlib.pyplot as plt # Change implemented from Code Review suggestion from Medhnaa Saran 

# This is a fruit themed word guessing game!

def select_word():
    words = ['apple', 'banana', 'guava', 'mango', 'grape', 'strawberry'] # Word bank of fruits!
    return random.choice(words)

# The player guesses the letter, and the program determines if it is correct or not. 
def player_guess(word, letters_guessed):
    guess = input("Guess a letter: ").lower()
    letters_guessed.add(guess)
    occurrences = word.count(guess)
    if occurrences > 0:
        print(f"Correct! '{guess}' appears {occurrences} time(s) in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word.")

# This is the basis of the game and allows a certain number of attempts 
# It forces the player to remember which letters they have guessed. 
def play_game(number_players):
    word = select_word()
    letters_guessed = set()
    attempts = 0
    word_guesses = 0


    print("Welcome to Riya's Word Guessing Game!")
    print("Try to guess the fruit.")
    print("The length of the word is:", len(word))


    while True:
        for player in range(1, number_players + 1):
            print(f"\nPlayer {player}'s turn:")
            player_guess(word, letters_guessed)
            attempts += 1


            if all(letter in letters_guessed for letter in word):
                print(f"Congratulations! Player {player} guessed the word!")
                print(f"The word was '{word}'.")
                print(f"Number of attempts: {attempts}")
                return


            if attempts % 3 == 0:
                word_guesses += 1
                if word_guesses == 4:
                    print("Sorry, you've reached the maximum number of word guesses.")
                    print(f"The word was '{word}'.")
                    return

# Graph the scores of the players           
def plot_scores(scores):
    players = list(scores.keys())
    scores_values = list(scores.values())

    plt.bar(players, scores_values, color='skyblue')
    plt.xlabel('Players')
    plt.ylabel('Attempts')
    plt.title('Word Guessing Game Scores')
    plt.show()

# Enter the how many players are playing 

if __name__ == "__main__":
    number_players = int(input("Enter the number of players: "))
    play_game(number_players)


