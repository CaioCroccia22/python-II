from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma listas
fruits = ["Maçã", "Banana", "Uva", "Pera", "Uva", "Banana", "Uva", "Maçã", "Pera"]

print(fruits)
print(Counter(fruits))


# 2 - Utilizando Tupla Nomeada
game = namedtuple('game', ['name', 'price', 'rate'])
g1 = game("Fifa23","300", "5" )
g2 = game("Mario", "200", "4")
g3 = game("World of Zelda", "150", "5")

print(g1)
print(g2)
print(g3)

# 3 - Ordenando dicionários
students = {"Pedro":23, "Ana": 21, "Ronaldo": 26, "Janaina": 25}

order = sorted(students.items(), key=itemgetter(0))
print(students)
print(order)


# 4 - Utilizando fila com ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10) #Adiciona o da esquerda
print(deq)
deq.popleft()#Remove o da esquerda
deq.pop() #Remove do final
print(deq)

