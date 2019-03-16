from data import DICTIONARY, LETTER_SCORES
import random

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as infile:
        word_list = [x.strip() for x in infile.readlines()]
    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter.isalnum():
            score += LETTER_SCORES[letter.upper()]
    return score


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = ''
    max_word_val = 0
    for word in words:
        if calc_word_value(word) > max_word_val:
            max_word_val = calc_word_value(word)
            max_word = word
    return max_word


if __name__ == "__main__":
    word_list = load_words()
    sample_words = []
    for _ in range(10):
        sample_words.append(random.choice(word_list))
    for word in sample_words:
        print("{}: {}".format(word, calc_word_value(word)))
    print("from DICTIONARY: {}".format(max_word_value()))