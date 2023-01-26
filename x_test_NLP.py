import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = ['I love my dog',
             'I love my cat',
             'You love my dog!'
             'Do you think my dog is amazing?'
             ]

print (sentences)

tokenizer = Tokenizer(num_words=100, oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)
print ('\nWord Index = {}'.format(word_index))
print ('\nSequences = {}'.format(sequences))


