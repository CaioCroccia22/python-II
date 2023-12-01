"""
Modulo HashLib 
Tem por objetivo criptografar textos

"""

import hashlib

# #Verificar os algoritmos disponiveis
# print(hashlib.algorithms_available)
# """
# {'sha3_224', 'sha512_256', 'sha256', 'sha384', 'sha512', 'sha1', 'shake_2o\Python\Módulo 2>56', 'blake2s', 'sha224', 'blake2b', 'shake_128', 'sha3_512', 'sha3_256', 'sm3', 'sha512_224', 'ripemd160', 'sha3_384', 'md5', 'md5-sha1'} 
# """

# #Algoritmos disponiveis de acordo com o SO
# print(hashlib.algorithms_guaranteed)

#Utilizando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "O caio é muito legal".encode()
algorithm.update(message)
print(algorithm.hexdigest())