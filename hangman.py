import random, math

WORDS = ["HI", "LANSI", "PATRICK", "LARGE", "FANTASTIC", "SCIENCE", "COMPUTER"]

class Hangman:
    def __init__(self):
        self.word = ''
        self.guessed_letters = []
        self.word_underscored = ''
        self.letters_left = 0
        self.guessed = False

    def get_word(self):
        index = int(math.floor(random.uniform(0, 1) * 10) % len(WORDS))
        # print(index)
        word = WORDS[index]
        # print(word)
        return word

    def get_underscores(self):
        self.word_underscored = '_' * len(word)
        self.letters_left = len(word)

    def update_word_underscored(self, x):
        updated_underscore = list(self.word_underscored)
        for i in range(len(word)):
            if x == word[i]:
                updated_underscore[i] = x
                self.letters_left -= 1
            elif not updated_underscore[i] == '_':
                continue
            else:
                updated_underscore[i] = '_'
        self.word_underscored = updated_underscore
        return self.word_underscored

    def add_letter(self, x):
        self.guessed_letters.append(x)


if __name__ == '__main__':
    hangman = Hangman()
    word = hangman.get_word()
    hangman.get_underscores()
    while not hangman.guessed:
        userGuess = raw_input("The word has {} characters. What letter would you like to guess?".format(len(hangman.word_underscored))).upper()
        if not len(userGuess) == 1:
            print("Please only guess 1 letter.")
        else:
            if userGuess in hangman.guessed_letters:
                print("You've already guessed that letter.")
            elif userGuess in word:
                hangman.add_letter( userGuess)
                print("Yes! {} is in word.".format(userGuess))
                print("You have the following: {}".format(hangman.update_word_underscored(userGuess)))
            else:
                print("{} is not in the word.".format(userGuess))

        if hangman.letters_left == 0:
            print("Congrats! You guessed the entire word!")
            hangman.guessed = True