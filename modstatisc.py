import statistics

"""



"""

# 1 - Aplicar a média
print(statistics.mean([3, 2, 5, 8, 9]))

# 2 - Aplicar a mediana 
print(statistics.median([1, 2, 4, 5, 6, 3, 5, 4]))

# 3 - Aplicar a moda
#valor que mais se repete
print(statistics.mode([1, 3, 3, 3, 4, 5, 6]))

# 4 - Desvio padrão
"""
Quanto mais próximo de 0 for o desvio padrão
significa que os dados do conjunto estão menos dispersos
"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))