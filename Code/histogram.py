# writing a program that keeps track of the least/most frequent words
# keeps track of how many different words used
# tracks average frequency of words
from sys import argv
# function that takes a source text argument and returns a histogram data structure
# that stores each unique word and frequency
def histogram(file):
    histogram = {}
    with open(file,'r') as f:
        words = f.read().splitlines()
    for word in words:
        word = word.lower()
        if word in histogram.keys():
            histogram[word] += 1
        else:
            histogram[word] = 1
    return (histogram)


# function that takes histogram argument and returns count of unique words
def unique_words(histogram):
    return len(histogram.keys())
# function that takes a word and histogram argument and returns word frequency
def frequency(search,histogram):
    if search.lower() in histogram.keys():
        return histogram[search.lower()]
    else:
        return 0

if __name__ == '__main__':
    search = argv[1]
    h = histogram('despacito.txt')
    print(histogram('despacito.txt'))
    print(unique_words(h))
    print(frequency(search,h))


