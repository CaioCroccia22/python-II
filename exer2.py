"""
Verificar conteúdo da String
-> Escreva um programa em python para verificar se uma string
contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9 )

"""

import re

text = input("Digite a string que deseja analisar: \n")
pattern1 = '[a-z]'
pattern2 = '[A-Z]'
pattern3 = '[0-9]'
for t in text:
    if re.findall(pattern1, text):
     print('ok')
    elif re.findall(pattern2, text):
     print('ok')
    elif re.findall(pattern2, text):
     print('ok')
    else:
      print('não tem!')