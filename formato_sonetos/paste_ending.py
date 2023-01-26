#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from silabizer import *
import numpy as np


# In[8]:


#df_versos = pd.read_excel('versos_potenciales.xlsx')
#df_versos = pd.read_excel('versos.xlsx')
df_versos = pd.read_csv('output_v3_15_versos.csv')

df_versos.columns = ['waste', 'verse']
del df_versos['waste']
df_versos['terminacion'] = 'NULL'

s = silabizer()

for w in range(df_versos.shape[0]):
    line = df_versos.iloc[w]['verse']
    print(line)
    word = line.split()[-1]
    print(word)
    d = dict_silabas_one_word(word, s)
    sil = s(word)
    print(sil)
    df_versos['terminacion'].iloc[w] = sil
    
#df_versos.to_excel('output_v5_20_versos_potenciales_con_terminacion.xlsx')
df_versos.to_csv('output_v3_15_versos_potenciales_con_terminacion.csv')

#df_versos.to_csv('versos_potenciales_con_terminacion.csv')


# In[ ]:




