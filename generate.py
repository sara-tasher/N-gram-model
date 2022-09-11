import pickle
from random import choice
from numpy import random

def load_model(way):
    with open('model/' + way +'.pickle', 'rb') as f:
        dict = pickle.load(f)
    return dict

def generate(seed='', length = 40, dict = {}, prefix_count = 2, randomising_number = 21):
    answer = []
    random.seed(randomising_number)
    if seed == '':
        rand_pref = choice(list(dict.keys()))
        for word in rand_pref:
            answer.append(word)
    else:
        for word in seed.split():
            answer.append(word.lower())
    try:
        for i in range(len(answer),length):
            last_words = tuple(answer[i-prefix_count:])
            rand = int(random.choice(len(dict[last_words]), 1, p=list(map(lambda x: x[1], dict[last_words]))))
            answer.append(dict[last_words][rand][0])
    except Exception:
        print("Error, there are not enough words to generate text with length", length)


    print(*answer)