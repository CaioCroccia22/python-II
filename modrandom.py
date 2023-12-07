import random

#  1 - Selecionar o valor aleatório de uma lista
list = [1, 2, 4, 4, 5, 6, 6, 6, 6, 6]
print(random.choice(list))


# 2 - Gera um numero aleatorio em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

# 3 - Seleciona caracter aleatorio de uma string
name = 'curso pyhton'
r2 = random.choices(name)
print(r2)

# 4 - Selecionar mais de um valor aleatorio
# Sintaxe -> random.sample(sequencia, tamanho)
print(random.sample(list, 2))
print(random.sample(list, 3))