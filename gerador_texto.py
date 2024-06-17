import numpy as np

bolsonaro = open(r'bolsonaro.txt', encoding='utf8').read()

corpus = bolsonaro.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])

pairs = make_pairs(corpus)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(corpus)
chain = [first_word]
n_words = 25

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

' '.join(chain)
print(' '.join(chain))