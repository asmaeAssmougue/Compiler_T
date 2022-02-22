# -*- coding: utf-8 -*-


import ply.yacc as yacc
from ply import lex
from typing import Any

# List of token names.   This is always required

tokens = [
    'INT',
    'FLOAT',
    # Numbers
    'PLUS',
    'MINUS', 
    'TIMES',
    'DIVIDE', # operations
    'MODULO',
    
    # Parentheses and brackets and braces
    'IDENTIFICATEUR',
    #'BOOLEAN',
    'STRING',
    'AYTSSAWA',
    'LPAREN','LRPAREN',
    'DE',
    'N3AD',
    'NO9TAFASSILA',
    #'boolean',
    #comments
    'COMMENT',
    'FASILA',
     'ZAYDYAN',
     'NA9ESYAN',
     'literals',
     'RZAMLAMA',
     '9ENLAMA',
     '9ENLMA3E9OFA',
     'RZAMLMA3E9OFA',
     'SUP', 
     'INF', 
     'ATWLIKATSSAWI', 
     'INFEQUALS', 
     'SUPEQUALS', 
     'ORAYTSSAWA' # comparison ops'
     
  
]
#les mots reserves
reserved = {
    
     'oraythrak': 'ORAYTHRAK', #static
     'skchem':'SKCHEM',        #include
     'red':'RED',              #return
     'ilagfasil':'ILAGFASIL',  #double
     'ihtomach':'IHTOMACH',    #elseif
     'ikhwa':'IKHWA',          #void
     'amassen' : 'AMASSEN',    #until
     'khetwa' : 'KHETWA',      #le pas
      'hawel':'HAWEL',         #try
      'amezt':'AMEZT',         #catch
      'gherte':'GHERTE',       #scanf
      'foughe':'FOUGHE',       #break
      
      'kemal':'KEMAL',         #continue
      'awdet':'AWDET',         #for
      'mahed':'MAHED',         #while
      'ara':'ARA',             #print
      'ihtoriga':'IHTORIGA',   #else
      'ihiga':'IHIGA',         #if
      'akhiran' : 'AKHIRAN',   #finally
      'isha' : 'ISHA',         #true
       'orisha' : 'ORISHA',    #false
       'switch' : 'SWITCH',    #switch
       'case' : 'CASE',        #case
       'class' : 'CLASS',      #class
       'ta3rif': 'TA3RIF',     #def
       'sker' : 'SKER',        #do
       'extends':'EXTENDS',
       'private':'PRIVATE',
       'public':'PUBLIC'
}
tokens = tokens + list(reserved.values())




#regular expression
t_9ENLMA3E9OFA =r'\]'
t_RZAMLAMA=r'\{'
t_FASILA = r'\,'

t_literals=r'\:|\.'
t_RZAMLMA3E9OFA=r'\['
t_9ENLAMA=r'\}'
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
t_SUP = r'>'
t_INF = r'\<'
t_INFEQUALS = r'\<\='
t_SUPEQUALS = r'\>\='
t_ZAYDYAN = r'\+\+'
t_NA9ESYAN = r'--'
t_AYTSSAWA = r'\=\='   #egaleComp
t_ORAYTSSAWA = r'\!\='
t_ATWLIKATSSAWI = r'\='  #affectation
t_NO9TAFASSILA = r'\;'
# new line defintion
t_SKER = r'sker'
t_RED=r'red'
t_IHIGA=r'ihiga'
t_IHTORIGA=r'ihtoriga'
t_ARA=r'ara'
t_MAHED=r'mahed'
t_AWDET=r'awdet'
t_KEMAL=r'kemal'
t_FOUGHE=r'foughe'
t_GHERTE=r'gherte'
t_AMEZT=r'amezt'
t_HAWEL=r'hawel'
t_AMASSEN=r'amassen'
t_IKHWA=r'ikhwa'
t_IHTOMACH=r'ihtomach'
t_ILAGFASIL=r'ilagfasil'
t_KHETWA = r'khetwa'
t_SWITCH = r'switch'
t_CASE = r'case'
t_TA3RIF = r'ta3rif'
t_SKCHEM=r'skchem'
t_ORAYTHRAK=r'oraythrak'
t_CLASS= r'class'
t_EXTENDS=r'extends'
t_PRIVATE=r'private'
t_PUBLIC=r'public'



def t_ISHA(t):
    r'isha'
    t.value = True
    return t

def t_ORISHA(t):
    r'orisha'
    t.value = False
    return t

 # Define a rule so we can track line numbers
def newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)
   
def t_STRING(t):
    # [^"] : means any character except ", this way "hello" + "there" wont be considered a "String" but "string" + "string"
    #any lines between "" or '' can be written * and they are considred string
    #exept for " or ' example "the"re" or 'th're' we will have both the and re as strings and one ' or " detected ilegal 
    r'("[^"]*")|(\'[^\']*\')'
    if t.value[0] == '"':
        t.value = t.value[1:-1]
    elif t.value[0] == "'":
        t.value = t.value[1:-1]
    return t  

def t_COMMENT(t):
    r'\#.*|\$\$.*|\$.*'
     #print("comment detected")
    pass
   
def t_LPAREN(t):
      r'\('
    
def t_LRPAREN(t):

     r'\)'

def t_INT(t):
   r'\d+'
   t.value = int(t.value)    
   return t

def t_FLOAT(t):
    r'\d+\[[.]\d+'
    t.value = float(t.value)
    return t


def t_IDENTIFICATEUR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFICATEUR')    # Check for reserved words
    return t

def t_MINUS(t):
     r'-'  
     return t
     
def t_DIVIDE(t):
      r'/'      
      return t
  
def t_TIMES(t):
     r'\*'
     return t
 
def t_PLUS(t):
    r'\+'
    return t

def t_MODULO(t):
    r'\%'
    return t


def t_DE(t):
    r'\&& | de'
   

def t_N3AD(t):
    r'N3ad'

# Error handling rule
def t_error(t):
      print("ila ya lkhata 7amass nster : ", t.lineno)
      print("orizri wad '%s'" % t.value[0])
      t.lexer.skip(1)

lexer = lex.lex(debug=True)
# while True:
#    data=input("skechem kra :")
#    lexer.input(data)
#    while True:
#        tok=lexer.token()
#        if not tok:
#           break
#        print(tok)