import random

word_list = ["apple", "bannana", "orange", "kiwi", "strawberry"]
print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Opps! that is not a valid input.")