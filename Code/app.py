from flask import Flask
from histogram import histogram
from sample import sample
from markov import MarkovChain

app = Flask(__name__)


@app.route('/')
def generate_words():
    #build a histogram
    # my_file = open("despacito.txt","r")
    lines = "one fish two fish red fish blue fish"
    my_histogram = histogram(lines)
    word_list = []
    for line in lines:
        for word in line.split():
            word_list.append(word)

    word = sample(my_histogram)
    #return word

    sentence = ""
    num_words = 10
    # for i in range(num_words):
    #     word = weighted_sample(my_histogram)
    #     sentence += " " + word
    markovChain = MarkovChain(word_list)
    sentence = markovChain.walk(num_words)
    print("sentence", sentence)
    return sentence
if __name__ == '__main__':
    app.run(debug=True)

