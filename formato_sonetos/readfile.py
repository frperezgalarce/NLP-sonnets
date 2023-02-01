from silabizer import *
from check import *
import pandas as pd


def read_source():
    with open('output_v3_15.txt') as f:
        lines = f.readlines()
    return lines

def verses_by_line(lines):
    verses = []
    for l in lines:
        words = l.split()
        verses = createverses(silabas=11, line = l, verses= verses)
    return verses

def export_verses(verses):
    #pd.DataFrame(verses, columns=['endecasílabo']).to_excel('versos.xlsx')
    pd.DataFrame(verses, columns=['endecasílabo']).to_csv('output_v3_15_versos.csv')



