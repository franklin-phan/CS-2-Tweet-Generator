import random
from sys import argv


def dictionary_words(number):
    """Takes a random selection of number of words and outputs a sentence"""
    # f = open('/usr/share/dict/words','r')
    picked_words = []
    with open('/usr/share/dict/words','r') as f:
        words = f.read().splitlines()
    while number > len(picked_words):
        random_index = random.randrange(len(words))
        picked_words.append(words[random_index])
    return picked_words
if __name__ == '__main__':
    number = int(argv[1])
    print (dictionary_words(number))

