import random
import sys

def rearrange(words_list):
    for i, word in enumerate(words_list):
        rand_index = random.randint(0, len(words_list) - 1)
        words_list[i] = words_list[rand_index]
        words_list[rand_index] = word
    return words_list


if __name__ == "__main__":
    words_list = []

    for arg in range(1, len(sys.argv)):
        words_list.append(sys.argv[arg])

    shuffled_list = rearrange(words_list)
    print(shuffled_list)