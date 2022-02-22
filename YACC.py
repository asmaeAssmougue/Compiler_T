# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 17:49:56 2022

@author: HP
"""
'start'
import ply.lex as lex
import ply.yacc as yacc
import LEX
tokens = LEX.tokens
variables={}    
precedence = (
    ('left','ATWLIKATSSAWI'),
    ('left', 'PLUS', 'MINUS'),
   ('left', 'TIMES', 'DIVIDE'),
   ('left', 'N3AD', 'DE'),
  
   ('nonassoc', 'SUP', 'INF', 'SUPEQUALS', 'INFEQUALS', 'AYTSSAWA'),
    ( 'nonassoc', 'UMINUS' )

)



#affectation
def p_aytssawa( p ) :    
    'expr : IDENTIFICATEUR ATWLIKATSSAWI INT'
    p[0] = p[1] = p[3]
    variables.update({p[1] : p[3]})
    
#input    
def p_gherte(p):
      'expr : GHERTE RZAMLMA3E9OFA statement 9ENLMA3E9OFA NO9TAFASSILA'    
      
      p[0]=("we received the value",p[3])

#print
def p_print(p):
    'expr : ARA RZAMLMA3E9OFA statement 9ENLMA3E9OFA NO9TAFASSILA'
    p[0] = (p[3])
    
#instruction    
def p_statement(p):
    '''statement : expr       
                               | IDENTIFICATEUR
                             
                             
                              
                              
    ''' 
    p[0] = p[1]
    
#addition    
def p_add(p) :
    'expr : expr PLUS expr'
    p[0] = p[1] + p[3]
    
#int    
def p_INT(p) :
    
    'expr : INT'
    p[0] = (p[1])

#soustraction    
def p_sub( p ) :
    'expr : expr MINUS expr'
    p[0] = p[1] - p[3]
 
#lecture    
def p_lecture(p):
   '''expr : expr  expr
                             
                             | expr  statements
                             
                                                    '''
   p[0]=(p[1],p[2])     
#div/mult  
def p_mult_div(p) :
    '''expr : expr TIMES expr
            | expr DIVIDE expr'''

    if p[2] == '*' :
        p[0] = p[1] * p[3]
    else :
        if p[3] == 0 :
            print("Can't divide by 0")
            raise ZeroDivisionError('integer division by 0')
        p[0] = p[1] / p[3]
        
#les parentheses
def p_parens(p) :
    'expr : LPAREN expr LRPAREN'
    #le resultat a retourner est l expression a lint des parenteheses
    p[0] = p[2] 
    
#modulo   
def p_MODULO(p) :
    
        'expr : expr MODULO expr'
        if p[3] == 0 :
           print("Can't divide by 0")
           raise ZeroDivisionError('integer division by 0')
        p[0] = p[1] % p[3] 
        
def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'
    p[0] = - p[2]  
       
#empty 
def p_empty(p):
     'empty :'
     pass
 
#void    
def p_void(p):
   '''expr : IKHWA RZAMLMA3E9OFA  9ENLMA3E9OFA '''
   p[0]=0
   
#include   
def p_include(p):
    '''expr : SKCHEM  INF IDENTIFICATEUR SUP NO9TAFASSILA
             '''
    #le resultat a retourner est l expression a lint des parenteheses
    p[0]=print("ikchem mzyanne")
    
#return    
def p_return(p):
    
    '''expr : RED RZAMLMA3E9OFA IDENTIFICATEUR 9ENLMA3E9OFA  NO9TAFASSILA 
            | RED  expr NO9TAFASSILA  '''
    if len(p) == 4:
         
        p[0]=(p[2])
    else:   
        p[0]=(p[3])
  
#static    
def p_static(p):
    'expr : ORAYTHRAK  IDENTIFICATEUR NO9TAFASSILA '
    p[0]=(p[2])
   
    
# comment     
# def p_COMMENT(p):
#     'expr : COMMENT'  
#     p[0]=p[1]                     

#boolean
#its not known if we put it alone because its included in otherexpression as well so yacc does reconize alone
def p_boolean_statment(p):
   
    ''' boolean : ISHA  
                 | ORISHA
                         
    '''
    p[0] = p[1]

#list of instructions
def p_statements(p):
    ''' statements : statements statement
                   | statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]        
#parametres d'une fonction
def p_parameter(p):
    '''
    parameter : IDENTIFICATEUR
    '''
    p[0] = p[1]

#liste des parametres
def p_parameter_list(p):
    '''
        parameter_list : parameter
                       | parameter_list FASILA parameter
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if(not isinstance(p[1], list)):
            p[1] = [p[3]]
        else:
            p[1].append(p[3])
        p[0] = p[1]

#liste des  arguments 
def p_argument_list(p):
    '''
        argument_list : expr
                      | argument_list FASILA expr
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if(not isinstance(p[1], list)):
            p[1] = [p[3]]
        else:
            p[1].append(p[3])
        p[0] = p[1]
        
#définition des fonct
def p_func(p):
    '''
         expr : TA3RIF IDENTIFICATEUR RZAMLMA3E9OFA parameter_list 9ENLMA3E9OFA  RZAMLAMA  statements 9ENLAMA
         | TA3RIF IDENTIFICATEUR RZAMLMA3E9OFA 9ENLMA3E9OFA RZAMLAMA statements 9ENLAMA
    '''
    if(len(p) == 8):
        p[0] = ('ta3rif', p[2], p[6])
    else:
        p[0] = ('ta3rif', p[2], p[4], p[7])
 
#appel de fonction
def p_appel_func(p):
    '''
    expr : IDENTIFICATEUR RZAMLMA3E9OFA argument_list 9ENLMA3E9OFA
               | IDENTIFICATEUR RZAMLMA3E9OFA  9ENLMA3E9OFA

    '''
    if(len(p) == 4):
        p[0] = ('appel_func', p[1])
    elif(len(p) == 5):
        p[0] = ('appel_func', p[1], p[3])
        
#if
#statemet ne doit pas contenir dans le print un mot reserve comm isha !!!   
def p_if(p):
     
   '''expr : IHIGA RZAMLMA3E9OFA expr 9ENLMA3E9OFA  RZAMLAMA  statements 9ENLAMA 
                        
            '''
 
   if p[3]==1:
      p[0]=p[6]
   else:
      print("orisha chert ")
# def p_incre(p):
     
#     '''expr : IDENTIFICATEUR ZAYDYAN 
                        
#             '''
 
   
#     p[0]=variables[p[1]]+1
#     variables[p[1]]=variables[p[1]]+1
   

#else if

def p_else(p):
     
    'expr : IHTOMACH  RZAMLAMA  statements  9ENLAMA  NO9TAFASSILA'
                 

    p[0]=p[3]
# private et public ne peuvent pas etre executee seul puisque on a pas une regle de prod mais une fois on l a defini ca marche 

def p_public(p):
     
    'expr : PUBLIC IDENTIFICATEUR NO9TAFASSILA'
                 

    p[0]=p[2]
def p_private(p):
     
    'expr : PRIVATE IDENTIFICATEUR NO9TAFASSILA'
                 

    p[0]=p[2]
def p_variable(p):
     
    ''' var : ORAYTHRAK IDENTIFICATEUR NO9TAFASSILA
                              | PRIVATE IDENTIFICATEUR NO9TAFASSILA
                              | PUBLIC IDENTIFICATEUR  NO9TAFASSILA
                             
                              
                                                     '''
def p_diffrent_variables(p):
    ''' vars : vars var
                   | var
    '''

def p_class(p):
     
  
          
    '''
        expr : CLASS IDENTIFICATEUR EXTENDS IDENTIFICATEUR   RZAMLAMA  vars TA3RIF IDENTIFICATEUR RZAMLMA3E9OFA parameter_list 9ENLMA3E9OFA  RZAMLAMA  statements 9ENLAMA 9ENLAMA
                      | CLASS IDENTIFICATEUR EXTENDS IDENTIFICATEUR   RZAMLAMA  vars TA3RIF IDENTIFICATEUR RZAMLMA3E9OFA 9ENLMA3E9OFA RZAMLAMA statements 9ENLAMA   9ENLAMA
    '''
    p[0]=("class",p[2],"created")


          
#Break
def p_foughe(p):
  
    '''expr : FOUGHE NO9TAFASSILA '''
    p[0] = p[1]  
    
#try{}   
def p_hawel_expr(p):
      'expr : HAWEL RZAMLAMA statements 9ENLAMA'   
      p[0] =p[3] 

#catch[]
def p_catchexpr(p):
    'expr : AMEZT RZAMLMA3E9OFA statement 9ENLMA3E9OFA '
    print("hatinoufa yan lkhata2")
#for 
#le pas c 'est egal a la variable khetwa  amassen nombre c est le nombre lorsque l on atteneint on s 'arrete   
def p_command_for(p):
    '''expr : AWDET RZAMLMA3E9OFA IDENTIFICATEUR ATWLIKATSSAWI INT AMASSEN INT NO9TAFASSILA KHETWA AYTSSAWA INT 9ENLMA3E9OFA RZAMLAMA statements 9ENLAMA
    '''
  
    ret = []
    if p[7] > p[5]:
        i = 0
        while i < p[7]-p[5]:
            ret.append(p[14])
            i = i+int(p[11])
        p[0] = ret
    else:
        print("erreur index")

#comparison
def p_comparison(p):
    ''' expr : expr AYTSSAWA expr
                              | expr ORAYTSSAWA expr
                              | expr SUP expr
                              | expr INF  expr
                              | expr SUPEQUALS expr
                              | expr INFEQUALS expr
                                                     '''
                             
    if p[2] == '==':
            p[0] = p[1] == p[3]
    elif p[2] == '!=':
            p[0] = p[1] != p[3]
    elif p[2] == '>':
            p[0] = p[1] > p[3]
    elif p[2] == '<':
            p[0] = p[1] < p[3]
    elif p[2] == '>=':
             p[0] = p[1] >= p[3]
    elif p[2] == '<=':
             p[0] = p[1] <= p[3] 
#error 
def p_error(p):
   
    print("ila yan lkhata f '%s'" % p.value)  
   
 #continue   
def p_kemal(p):
  
    '''expr : KEMAL  NO9TAFASSILA '''
    p[0] = p[1]   
#floatDeclaration    
def p_floatdeclaration(p):
    
    '''expr : ILAGFASIL IDENTIFICATEUR NO9TAFASSILA 
             '''
    p[0]=(p[2])  
#while    
def p_while(p):
    '''
    expr : MAHED  RZAMLMA3E9OFA expr  9ENLMA3E9OFA RZAMLAMA statements 9ENLAMA

    '''
    if p[3]==1:
      p[0] = ( p[6])
    else:
      print("ortsofit ichert!!")
#do while    
# def p_doWhile(p):
#     '''
#     expr :  SKER  RZAMLAMA statements 9ENLAMA MAHED  RZAMLMA3E9OFA expr 9ENLMA3E9OFA
#     '''
#     if p[7]==1:
#       p[0] = (p[3])
#     else:
#       print("tsofit ichert!!")

    
#lancer le parser

while True:
  try:
    s = input('T++ >')
  except EOFError:
   break
  if not s: continue
  parser = yacc.yacc()
  result = parser.parse(s)
  print (result);
