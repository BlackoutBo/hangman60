import random
word_list = ["apple", "bannana", "orange", "kiwi", "strawberry"]
word = random.choice(word_list)

class hangman:
    def __init__(self, word_list, num_lives=5):
        
        self.word = word
        self.word_guessed = ["_" for _ in self.word]  
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
      
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess 
            self.num_letters -= 1
            print("Word: " + " ".join(self.word_guessed))
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives remaining")
         
    def ask_for_input(self):
        while True:
            guess = input("Guess a Letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
        
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()

        else:
            if game.num_lives != 0 and game.num_letters == 0:
                print("Congratulations. You won the game!")
                break

play_game(word_list)