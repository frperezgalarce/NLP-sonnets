

from tensorflow.keras.preprocessing.text import Tokenizer


text_data=["Hello","Run", "Cat", "loro", "robert", "llanos", "Cat", "cat"]
print('\nArreglo incial:\n', text_data)

# Objeto Tokenizer
# char_level=True, va por caracter
# char_false, va por palabra
#tok = Tokenizer(char_level=True)
tok = Tokenizer(char_level=False)

# Se crea el indice de vocabulario basado en la frecuencia de las palabras
tok.fit_on_texts(text_data)

# Se pasa del texto a la sequencias (histograma*)
sequences = tok.texts_to_sequences(text_data)
print('\nToken: texts to sequences:\n', sequences)

# Tamanio del aphabeto
alphabet_size = len(tok.word_index)
print('\nToken: word_index:\n', alphabet_size)

# Se resconstruye la sequencia en texto
reconstructed_text = tok.sequences_to_texts(sequences)
print('\nToken: sequennce to texts:\n', reconstructed_text)

