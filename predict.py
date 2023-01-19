from keras.models import load_model
import sys
import random
import numpy as np
from keras.preprocessing.text import Tokenizer
from utils import *

text_len = 475749
print('Text length: ', text_len)

n=25 #input length
m=1 #output length

samples = text_len-n
alphabet_size = 69
x = np.zeros((samples, n, alphabet_size), dtype=np.bool)
model = load_model('weights.hdf5')
chars_to_generate = 50




print('predict')


doc = loadDocument('result.txt')
doc = applyFilter(doc)

tokenizer = Tokenizer(lower=True, char_level=True)
tokenizer.fit_on_texts(doc)

alphabet_size = len(tokenizer.word_index)
print('alphabet_size: ', alphabet_size)
keys = list(tokenizer.word_index.keys())
for key in keys:
	tokenizer.word_index[key] -= 1


for k in range(1000):
    temperature = 0.2
    start_index = random.randint(0, len(x)-1)
    generated = ''
    one_hot_sentence = x[start_index]
    text_sentence = encodedTextToString(one_hot_sentence, keys)
    generated += text_sentence
    sys.stdout.write(generated)
    for i in range(chars_to_generate):
            preds = model.predict(np.array([one_hot_sentence]), verbose=0)[0]
            next_char = oneHotArrayToChar(preds, keys, temperature=temperature)
            generated += next_char

            next_char_one_hot = np.zeros((alphabet_size))
            next_char_one_hot[tokenizer.word_index[next_char]] = 1
            one_hot_sentence = np.append(one_hot_sentence[1:],[next_char_one_hot],axis=0)

            sys.stdout.write(next_char)
            sys.stdout.flush()