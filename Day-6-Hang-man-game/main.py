import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["apple", "banana", "orange", "accident"]
random_index = random.randint(0, len(word_list) - 1)

generated_word = word_list[random_index]
print(generated_word)
word_length = len(generated_word)

line_list = []

lives = 6
print(stages[lives])

for line in range(word_length):
    line = "_"
    line_list.append(line)
print(line_list)

end_of_game = False

while not end_of_game:
    guess = input("guess a letter:")
    for position in range(word_length):
        letter = generated_word[position]
        if letter == guess:
            line_list[position] = guess

    if guess not in generated_word:
        print("lost a life")
        lives -= 1
        print(stages[lives])

        if lives == 0:
            end_of_game = True
            print("you lost!")

    else:
        print(line_list)

    if "_" not in line_list:
        end_of_game = True
        print("You have won!")

# hasLife = bool("true")
# life_count = 4

1  # generate a random word
2  # gen as many lines as the word
3  # ask user for a guess, make it lower case
4  # check if the guessed letter is in the gen word
5  # if so then find its index in the word, both lower and higher
6  # using both indices replace the "_" with the guess
7  # print the list of blanks with the guessed letter
8  # if guess is not in the word, loose a life, decrease life by 1
# if life become 0, print game over
9  # repeat 3 to 8 until all the blanks are filled

#
# while line_list.__contains__("_") and life_count != 0:
#     guess = input("please enter your guess\n").lower()
#     if generated_word.__contains__(guess):
#         lowest_index = generated_word.find(guess)
#         highest_index = generated_word.rfind(guess)
#         line_list[lowest_index] = guess
#         line_list[highest_index] = guess
#         print(line_list)
#     else:
#         print("lost a life")
#         life_count -= 1
#         if life_count == 0:
#             hasLife = bool("false")
#             print("game over")
