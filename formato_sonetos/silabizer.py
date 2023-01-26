import re


class char():
    def __init__(self):
        pass
    
class char_line():
    def __init__(self, word):
        self.word = word
        self.char_line = [(char, self.char_type(char)) for char in word]
        self.type_line = ''.join(chartype for char, chartype in self.char_line)
        
    def char_type(self, char):
        if char in set(['a', 'á', 'e', 'é','o', 'ó', 'í', 'ú']):
            return 'V' #strong vowel
        if char in set(['i', 'u']):
            return 'v' #week vowel
        if char=='x':
            return 'x'
        if char=='s':
            return 's'
        else:
            return 'c'
            
    def find(self, finder):
        return self.type_line.find(finder)
        
    def split(self, pos, where):
        return char_line(self.word[0:pos+where]), char_line(self.word[pos+where:])
    
    def split_by(self, finder, where):
        split_point = self.find(finder)
        if split_point!=-1:
            chl1, chl2 = self.split(split_point, where)
            return chl1, chl2
        return self, False
     
    def __str__(self):
        return '<'+self.word+':'+self.type_line+'>'
    
    def __repr__(self):
        return '<'+repr(self.word)+':'+self.type_line+'>'

class silabizer():
    def __init__(self):
        self.grammar = []
        
    def split(self, chars):
        rules  = [('VV',1), ('cccc',2), ('xcc',1), ('ccx',2), ('csc',2), ('xc',1), ('cc',1), ('vcc',2), ('Vcc',2), ('sc',1), ('cs',1),('Vc',1), ('vc',1), ('Vs',1), ('vs',1), ('vxv',1), ('VxV',1), ('vxV',1), ('Vxv',1)]
        for split_rule, where in rules:
            first, second = chars.split_by(split_rule,where)
            if second:
                if first.type_line in set(['c','s','x','cs']) or second.type_line in set(['c','s','x','cs']):
                    #print 'skip1', first.word, second.word, split_rule, chars.type_line
                    continue
                if first.type_line[-1]=='c' and second.word[0] in set(['l','r']):
                    continue
                if first.word[-1]=='l' and second.word[-1]=='l':
                    continue
                if first.word[-1]=='r' and second.word[-1]=='r':
                    continue
                if first.word[-1]=='c' and second.word[-1]=='h':
                    continue
                return self.split(first)+self.split(second)
        return [chars]
        
    def __call__(self, word):
        return self.split(char_line(word))


def tipoAcento(palabra): #este método encuentra el tipo de acento 
    tilde = False
    ub = 100
    sil = 100
    silabas = s(palabra)
    #print(silabas)
    for i in range(0, len(silabas)):
        ss = silabas[i]
        r = re.findall('[^A-Za-z0-9]',str(ss).replace('<','').replace('>','').replace(':',''))
        if r: 
            ub = len(silabas)-i
            sil = i+1
            #print(r)
            #print(ub)
            tilde = True
    
    if tilde == False: 
        letras = list(palabra)   
        ultima = letras[-1]
        if ultima in ['n', 's', 'a', 'e', 'i', 'o', 'u']:
            ub = 2
            sil = len(silabas) -ub +1
        else: 
            ub = 1
            sil = len(silabas) -ub +1
    return [tilde, ub, sil]


def terminacion(palabra, s): 
    term = s(palabra)[len(s(palabra))-1]
    return term


def contarsilabas(palabra, s): 
    palabra = len(s(palabra))
    return palabra

def dict_silabas_one_word(w, s): 
    d = {}
    n = contarsilabas(w, s)
    d[w] = n
    return d 

def dictSilabas(df): 
    d = {}
    for key in range(0,df.shape[0]):
        try:
            n = contarsilabas(df.iloc[key]['word'])
            d[df.iloc[key]['word']] = n
        except: 
            print(df.iloc[key]['word'])
    return d 