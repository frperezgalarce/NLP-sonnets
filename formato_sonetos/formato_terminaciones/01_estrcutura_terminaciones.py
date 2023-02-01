#!/usr/bin/env python3

from collections import defaultdict

import random
import json
import sys
import os
import pandas as pd


def cut_syllable (data):
    i=3
    for c in data:
        if (c == "\'"):
            break
        i+=1
    return i


def read_source(filename):
    with open(filename, 'r') as data_file:
        text = data_file.readlines()
    return text


def obtain_finalSyllabes(text):
    lines = []
    final_syls = []
    i = 0
    for line in text:

        tmp_line = line[3:]
        cut_line = cut_syllable(tmp_line)
        #sys.stdout.write (line[3:cut_line]+"\n")
        final_syl = line[3:cut_line]
        final_syls.append(final_syl)
        #print ("#####################")
        i += 1
    print ("terminaciones: ", i)

    return final_syls


def finalSyllabes_to_dict (final_syls):
    text_verses = pd.read_csv("00_obtener_terminaciones.tmp_100.csv")
    counter = {}
    verses_2 = defaultdict(list)
    #counter = {"qa": 1}
    i=0
    for syl in final_syls[1:]:
        if syl in counter.keys():
            tmp = counter[syl]
            tmp += 1
            counter[syl] = tmp
            verses_2[syl].append(text_verses.loc[i].verse)

        else:
            counter[syl] = 1
            #print (syl, text_verses.loc[i].verse)
            verses_2[syl].append(text_verses.loc[i].verse)

        i += 1

    return counter, verses_2

def to_json (name, dictio):
    with open(name+".json", "w", encoding = "utf-8") as outfile:
        json.dump(dictio, outfile)


def create_sonnets (verses_2, city="santiago"):
    print ("\n\nXXXXXXXXXXXXXXXXXXXXXX")
    
    #some = "ción"
    #some1 = "da"
    #some2 = "so"
    #some3 = "bio"

    some = random.choice(list(verses_2.keys()))
    some1 = random.choice(list(verses_2.keys()))
    some2 = random.choice(list(verses_2.keys()))
    some3 = random.choice(list(verses_2.keys()))

    #print (random.choices(list(verses_2[some]), k=4))
    #print (random.choices(list(verses_2[some1]), k=4))
    #print (random.choices(list(verses_2[some2]), k=3))
    #print (random.choices(list(verses_2[some3]), k=3))

    list_A = random.choices(list(verses_2[some]), k=4)
    list_B = random.choices(list(verses_2[some1]), k=4)
    list_C = random.choices(list(verses_2[some2]), k=4)
    list_D = random.choices(list(verses_2[some3]), k=4)

    sonnets = list_A[0]+"\n"+list_B[0]+"\n"+list_B[1]+"\n"+list_A[1]+"\n\n"+list_A[2]+"\n"+list_B[2]+"\n"+list_B[3]+"\n"+list_A[3]+"\n\n"+list_C[0]+"\n"+list_D[0]+"\n"+list_C[1]+"\n\n"+list_D[1]+"\n"+list_C[2]+"\n"+list_D[2]

    print (sonnets)

    counter_city = "2"
    with open('verses/'+city+'/'+str(counter_city)+'.txt', 'w') as f:
        f.write(sonnets)



def main():

    filename="00_obtener_terminaciones.tmp_1.csv"
    text = read_source (filename)
    lines = obtain_finalSyllabes (text)
    dictionary, verses_2 = finalSyllabes_to_dict (lines)

    to_json("nnn", dictionary)
    to_json("bbb", verses_2)

    #print ("\n\nDICT: ", dictionary)
    #print ("\n\nDICT: ", verses_2)

    #city="santiago"
    for city in os.listdir('./verses'):
        #print (city)
        try:
            create_sonnets(verses_2, city)
        except:
            print ("Not found dir.")


if __name__ == "__main__":
    main()


