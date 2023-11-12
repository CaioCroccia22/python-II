"""
Módulos  - São arquivos em python que pode conter funções classes e variáveis
Eles podem ser utilizados via importação (import)
Eles também permitem a reutilização de código
"""
"""
Suas vantagens são a simplicidade, manutenbilidade no código
Um programa não precisa ser uma entidade única(monolito).
Isolamento no projeto de software

"""

import calc
# from calc import div

print(calc.sum(10, 2))
print(calc.sub(3, 5))
print(calc.mult(3, 5))
print(calc.div(10, 5))

"""
Módulo string 
Escrever um modulo em python para tratar algumas string que possua as seguintes funcionalidades:
1- Inverter apenas letras com indice par
2- Retornar apenas letras com indice par
3- Retornar apenas letras com indice impar
"""

import funcstrings

name = input("Digite uma frase: \n")

print(funcstrings.odd(name))
print(funcstrings.even(name))
print(funcstrings.reverse(name))