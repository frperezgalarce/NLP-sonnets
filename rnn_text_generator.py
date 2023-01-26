""" Text generator using LSTM
- by Vicente Opaso V.
"""
import sys
import random
import numpy as np


from utils import *
from keras import optimizers

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.callbacks import LambdaCallback
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.text import Tokenizer

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# -----------------------------
# Loading input
# -----------------------------

### Aca se puede entregar otro texto
doc = loadDocument('result_v6.txt')
doc = applyFilter(doc)


# Objeto token
tokenizer = Tokenizer(lower=True, char_level=True)

# Se crea el indice de vocabulario basado en la frecuencia de las palabras
tokenizer.fit_on_texts(doc)

alphabet_size = len(tokenizer.word_index)
print('\nalphabet_size: ', alphabet_size)

keys = list(tokenizer.word_index.keys())

for key in keys:
  tokenizer.word_index[key] -= 1

print('\nAlphabet: ', tokenizer.word_index)
sequence_of_int = tokenizer.texts_to_sequences([doc])[0]
text_with_one_hot_encoding = to_categorical(sequence_of_int, alphabet_size)

text_len = len(text_with_one_hot_encoding)
print('\nText length: ', text_len)

#n cantidad de caracteres por semilla
n=25 #input length
#m cantidad de caracteres que se predicen
m=1 #output length


#### hasta acá se cambian los pesos 38 - 54
samples = text_len-n

#representacion de cacarcteres con vectores
x = np.zeros((samples, n, alphabet_size), dtype=bool)
y = np.zeros((samples, m, alphabet_size), dtype=bool)

for i in range(samples):
  x[i]=text_with_one_hot_encoding[i:i+n]
  y[i]=text_with_one_hot_encoding[i+n:i+n+m]
  
y = np.squeeze(y) #delete the axis that have shape 1 (case m=1)

#### hasta aca funciona bien

# -----------------------------
# Building LSTM mode
# -----------------------------

print('\n\n######################################################')
print('###\t\t      build model     \t\t   ###')
print('######################################################\n\n')

#capas densas de keras
model = Sequential()
model.add(LSTM(128, input_shape=(n, alphabet_size), dropout = 0.2))

#(output de de la capa anterior debe calzar con el siguiente)
model.add(Dense(alphabet_size))

#n categorias pbb a cada caracter
model.add(Activation('softmax'))

# optimizador que no hay que cmabiar
#adam = optimizers.Adam(lr=0.0005)
adam = optimizers.Adam(learning_rate=0.0005)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
# funcion de perdida por ahi


# -----------------------------
# Building text generator
# -----------------------------

#(will be executed at the end of each epoch)
def on_epoch_end(epoch, logs):
  
  print()
  print('\n----- Generating text after Epoch: %d' % epoch)
  chars_to_generate = 20

  start_index = random.randint(0, len(x)-1)

  for temperature in [0.05]:
    print('\n----- temperature:', temperature)

    generated = ''
    one_hot_sentence = x[start_index]
    text_sentence = encodedTextToString(one_hot_sentence, keys)
    generated += text_sentence
    print ('generated: ', generated)
    print('\n----- Seed generator: "' + text_sentence + '"')
    sys.stdout.write(generated)

    for i in range(chars_to_generate):
      preds = model.predict(np.array([one_hot_sentence]), verbose=0)[0]
      next_char = oneHotArrayToChar(preds, keys, temperature=temperature)
      generated += next_char

      next_char_one_hot = np.zeros((alphabet_size))
      next_char_one_hot[tokenizer.word_index[next_char]] = 1
      one_hot_sentence = np.append(one_hot_sentence[1:],[next_char_one_hot],axis=0)

      #model.summary()
      sys.stdout.write(next_char)
      sys.stdout.flush()
    print()



# -----------------------------
# Training the model
# -----------------------------

weights_path = 'weights_v6_20.hdf5'
checkpointer = ModelCheckpoint(filepath=weights_path, verbose=1)
generator_callback = LambdaCallback(on_epoch_end=on_epoch_end)

batch_size, epochs = 64, 20
model.fit(x, y, batch_size=batch_size, epochs=epochs, callbacks=[checkpointer, generator_callback])

print('\nText length: ', text_len)
