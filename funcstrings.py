def reverse(word):
    return word[::-1]

"""
Relembrando fatiamento
[a:] - começo
[:b] - final
[::c] - Passo(condição)
Lembrando que o primeiro indice é 0
"""

def even(word):
   return word[::2]

def odd(word):
    return word[1::2]