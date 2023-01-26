from keras.models import load_model
import sys
import random
import numpy as np 
from keras.preprocessing.text import Tokenizer


### Determina la letra que se escoge para cambiar su estado a true
def oneHotArrayToChar(one_hot_array, keys, temperature=0.2, argmax=False):
	if argmax:
		return keys[one_hot_array.argmax()]
	index = sample(one_hot_array, temperature)#one_hot_array.argmax()
	return keys[index]
  

### Codifica el texto a string
def encodedTextToString(one_hot_text, keys):
	string = ""
	for one_hot_array in one_hot_text:
		char = oneHotArrayToChar(one_hot_array, keys, argmax=True)
		string += char
	return string
  
### Se carga el documento
def loadDocument(path):
    #f = open(path,'r', encoding = "ISO-8859-1")
    f = open(path,'r', encoding = "utf-8")
    doc = f.read()
    f.close()
    return doc.lower()

### Se aplican los filtros de caracteres
def applyFilter(doc, chars_ignored='"#$%&()*+-/<=>@[\]^_`{|}~\n\t'):
    for ch in chars_ignored:
        if ch == '\n':
          doc = doc.replace(ch,' ')
        else:
          doc = doc.replace(ch,'')
          doc = doc.replace('   ','  ')
    return doc

### 
def sample(preds, temperature=1.0):
	# helper function to sample an index from a probability array
	preds = np.asarray(preds).astype('float64')
	preds = np.log(preds) / temperature
	exp_preds = np.exp(preds)
	preds = exp_preds / np.sum(exp_preds)
	probas = np.random.multinomial(1, preds, 1)
	return np.argmax(probas)

