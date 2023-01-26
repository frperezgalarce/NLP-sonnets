#!/usr/bin/python


print('\n\n######################################################')
print('###\t\t    load libraries    \t\t   ###')
print('######################################################\n\n')

import sys
import random
import numpy as np

from utils import *
from keras.models import load_model
from keras.preprocessing.text import Tokenizer


### Se carga el modelo entrenado
print('\n\n######################################################')
print('###\t\t      load model       \t\t   ###')
print('######################################################\n\n')

model = load_model('weights_v6_20.hdf5')

#text_len = 475749
text_len = 1057381
#text_len = 7930

### n cantidad de caracteres por semilla
n=25 #input length

### m hace mas robusta la prediccion?
m=1 #output length

### Este parametro me complica por que es demasiado grande, vendría
### a ser un arreglo de 371.000 celdas*
### Por que restarle a un numero tan grande un numero tan chico
samples = text_len-n

### alphabet_size lo obtengo desde rnn_text_generator
#alphabet_size = 69

# esta variable luego se redefine, por lo que queda obsoleta
alphabet_size = 45


### Cantidad de caracteres por generar
### Al hacer más grande la cantidad de caracteres por linea, la predicción se hacía más mala.
chars_to_generate = 50

print('\n\n######################################################')
print('###\t\t\tPredict\t\t\t   ###')
print('######################################################\n\n')

print('Text length: ', text_len)
print('alphabet_size 1:', alphabet_size)

### Se carga el documento del modelo para la prediccion
doc = loadDocument('result_v6.txt')
doc = applyFilter(doc)

### Objeto tokenizer, char_level=True indica que se hara la representación del
### vocabulario por cada caracter
tokenizer = Tokenizer(lower=True, char_level=True)

### Se crea el indice de vocabulario basado en la frecuencia de las palabras
tokenizer.fit_on_texts(doc)

### Se obtiene el tamaño del alphabeto
alphabet_size = len(tokenizer.word_index)
print('alphabet_size 2:', alphabet_size)


### x es la representacion inicial de los caracteres en un arreglo 
### tridimensional de boleanos
x = np.zeros((samples, n, alphabet_size), dtype=bool)

### Se obtienen la lista de los caracteres tokenizados
keys = list(tokenizer.word_index.keys())


### Para partir desde 0 con las claves (por defecto parte 1 el token)
for key in keys:
	tokenizer.word_index[key] -= 1



### En la primera vuelta no escribe nada!!!
# Por cada verso
for k in range(1000):
#for k in range(1000):
	#print ('---------------')
	#print ('vuelta numero', k)
	temperature = 0.2
	start_index = random.randint(0, len(x)-1)
	generated = ''

	###  matriz con true y false que indica que caracter se esta prediciendo
	#print ('x: ', x)
	### Se obtiene aleatoriamente de que letra comenzar y se representa
	one_hot_sentence = x[start_index]
	#print ('\nlen(one_hot_sentence):', len(one_hot_sentence))

	### Esta funcion al parecer no hace nada, aunque deberia codificar el caracter
	### con el que comienza la predciccion
	text_sentence = encodedTextToString(one_hot_sentence, keys)
	#print ('text_sentence:', text_sentence)

	### Al agregar text_sentence quedan los espacios adelante en generated
	### test_sentence viene vacio
	#generated += text_sentence

	### genetated es cada verso generado
	#print ('generated:', generated)

	# Por cada letra
	for i in range(chars_to_generate):
		
		### Aca se predice desde el modelo
		preds = model.predict(np.array([one_hot_sentence]), verbose=0)[0]
		### Aca se obtiene el caracter desde la prediccion
		next_char = oneHotArrayToChar(preds, keys, temperature=temperature)
		generated += next_char
		#next_char += next_char

		#sys.stdout.write (str(i))
		#sys.stdout.write(next_char+' ')
		#sys.stdout.flush()
		
		### Arreglo de 0 de tamanio alphabeto
		next_char_one_hot = np.zeros((alphabet_size))

		### Que se cambia a 0?
		next_char_one_hot[tokenizer.word_index[next_char]] = 1

		### Hace contigua la prediccion
		one_hot_sentence = np.append(one_hot_sentence[1:],[next_char_one_hot],axis=0)

	# Se escribe el verso predicho
	sys.stdout.write(generated+'\n')
	sys.stdout.flush()


