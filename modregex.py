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

# 3 - buscando uma lista de caracteres dentro de uma frase
pattern = '[a-m]'
# [a-m] - significa que é de "a" até "m"
result = re.findall(pattern, text)
print(text)
print(result)


# 4 - Verificando o inicio de uma string
rule = r'^A'
# ^ - inicio
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrases: # Para cada frase que estiver na variavel phrases
    if re.match(rule, f):#Verifique se cada frase segue a variável regra
        print(f"Corresponde: {f}")#Se corresponder mostre qual frase=f