from silabizer import *
import numpy as np

def createverses(silabas=11,line='phrase', verses=[]): 
    counter = 0
    wordActualStart = 'c'
    wordActualEnd = 'c'
    wordPastEnd = 'c'

    s = silabizer()
    limit_lower = 0
    limit_upper = 0
    counter = 0

    words = line.split()

    for w in range(len(words)):
        d = dict_silabas_one_word(words[w], s)
        counter = counter + d[words[w]] 
        sil = s(words[w])  
        a = list(str(sil[-1]))    
        b = list(str(sil[0]))
        wordPastEnd = wordActualEnd       
        index1 = len(a)-2
        wordActualEnd = a[index1].lower()
        index2 = str(sil[0]).index(":")+1
        wordActualStart = b[index2].lower()      
        if(wordPastEnd == 'v' and wordActualStart == 'v'): 
            counter = counter - 1

        if counter == silabas: 
            verses.append(str(words[limit_lower:limit_upper]).replace("'", '').replace(',', ''))
            d_lower = dict_silabas_one_word(words[limit_lower], s)
            counter = counter -  d_lower[words[limit_lower]]
            limit_upper = limit_upper + 1
            limit_lower = limit_lower + 1
        elif counter > silabas:
            verses.append(str(words[limit_lower:limit_upper]).replace("'", '').replace(',', ''))
            d_lower = dict_silabas_one_word(words[limit_lower], s)
            counter = counter -  d_lower[words[limit_lower]]
            limit_upper = limit_upper + 1
            limit_lower = limit_lower + 1
        else:
            limit_upper = limit_upper + 1

    return verses
        

def sanitize(verse): 

    verse = (verse.replace(']','')
                 .replace('[', '')
                 .replace('.', '')
                 .replace(';','')
                 .replace(',', '')
                 .replace(':',''))

    return verse


def validate_verse(verses, silabas=11):
    validated_verses = []
    wordActualStart = 'c'
    wordActualEnd = 'c'
    wordPastEnd = 'c'
    s = silabizer() 
    for verse in verses: 
        verse = sanitize(verse)
        words = verse.split()
        counter = 0
        for word in words:
            d = dict_silabas_one_word(word, s)
            counter = counter + d[word] 
            sil = s(word)  
            a = list(str(sil[-1]))    
            b = list(str(sil[0]))
            wordPastEnd = wordActualEnd       
            index1 = len(a)-2
            wordActualEnd = a[index1].lower()
            index2 = str(sil[0]).index(":")+1
            wordActualStart = b[index2].lower()      
            if(wordPastEnd == 'v' and wordActualStart == 'v'):
                counter = counter - 1

        if (counter == silabas) and (d[word] > 1):
            validated_verses.append(verse)

    return validated_verses




        