import random
import sys
from dictogram import Dictogram

def sample(histogram):
    tokens = 0
    tokens += sum(histo.values())
    total_probability = 0
    dart = random.random()
    for key in histo.keys():
        prob = histo[key]/tokens
        if dart > total_probability and dart <=total_probability + prob:
            return key
        total_probability += prob

def sample_test(histogram):
    sample_list = [sample(histogram) for _ in range(10000)]
    sample_histogram = Dictogram(sample_list)

    for item in sample_histogram:
        print (f"{item}: {sample_histogram[item]}/10000")

if __name__ == "__main__":
    file = 'despacito.txt'
    with open(file, 'r') as f:
        words = f.read().split()
        histo = Dictogram(words)
    print (sample(histo))
    sample_test(histo)