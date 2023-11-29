"""
Módulo Regex

Analisa com dados textuais, quando é citado a palavra dados
logo vem a mente o big data, que seria o grande conjunto de dados
sendo boa parte do dados de big data sendo os dados não estruturados
sendo a maioria dados textuais

"""

import re

text = "Onebitcode: Transformamos pessoas em programadores sem limites"


# 1 - Indice  inicial e final da palavras
# O "r" significa que estamos trabalhando com uma string bruta (row string)
match = re.search(r'pessoas em programadores',text) #Procure a frase para mim na variável text

print(f'indice inicial {match.start()}')
print(f'indice final {match.end()}')


# 2 - Buscando o indice que tem um ponto
site = 'site: https://onebitcode.com'
# match = re.search(r'.', site)
match = re.search(r'\.', site)
print(match)

# 3 