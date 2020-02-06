# writing a program that keeps track of the least/most frequent words
# keeps track of how many different words used
# tracks average frequency of words
from sys import argv
# function that takes a source text argument and returns a histogram data structure
# that stores each unique word and frequency
def listogram(file):
    listogram = []
    with open(file,'r') as f:
        words = f.read().splitlines()
    for word in words:
        for inner_list in listogram:
            if inner_list[0] == word:
                inner_list[1] +=1
                break
        else:
            listogram.append([word,1])
    return (listogram)
# function that takes histogram argument and returns count of unique words
def unique_words(histogram):
    return len(histogram)
# function that takes a word and histogram argument and returns word frequency
def frequency(search,histogram):
    for inner_list in histogram:
        if inner_list[0] == search:
            return inner_list[1]
    else:
        return 0

if __name__ == '__main__':
    search = argv[1]
    h = listogram('despacito.txt')
    print(listogram('despacito.txt'))
    print(unique_words(h))
    print(frequency(search,h))


