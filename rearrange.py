import random
import sys


def rearrange(words_list):
    words_rearranged = []
    while len(words_list) > 0:
        random_index = random.randrange(len(words_list))
        item = words_list.pop(random_index)
        words_rearranged.append(item)
    return words_rearranged
if __name__ == "__main__":
   words_list = sys.argv[1:] #put arguments in a list
   print(rearrange(words_list))