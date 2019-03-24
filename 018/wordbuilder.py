from data import DICTIONARY, POUCH, LETTER_SCORES
import random
import itertools


def load_words():
    return DICTIONARY


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


def get_possible_dict_words(draw):
    permutations = _get_permutations_draw(draw)
    words = set()
    for word in permutations:
        if word.lower() in DICTIONARY:
            words.add(word)
    return words


def _get_permutations_draw(draw):
    permutations = []
    for i in range(1,len(draw)+1):
        permutations.extend([''.join(word) for word in 
            itertools.permutations(draw, i)])
    return permutations


def draw_letters():
    letters = []
    for _ in range(7):
        letters.append(random.choice(POUCH))
    return letters
    

def _validation(word, draw):
    if not word in DICTIONARY:
        raise ValueError("{} is not in dictionary".format(word))
    for letter in word:
        if not letter in draw:
            raise ValueError("The letter {} was not in the draw".format(letter))

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("letters", help="Letters in the rack")
    args = parser.parse_args()
    rack = args.letters
    print("Letter rack: {}".format(', '.join(rack)))
    possible_words = get_possible_dict_words(rack)
    optimal_word = max_word_value(possible_words)
    max_score = calc_word_value(optimal_word)
    print("Highest possible word: {} with a score of {}".format(
        optimal_word, max_score
    ))


if __name__ == '__main__':
    main()
    