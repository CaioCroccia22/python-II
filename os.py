import os

"""
Módulo OS 
Tem por objetivo automatizar algumas tarefas do Sistema Operacional utilizando a linguagem python
"""


# 1 - Consultar funcionalidades do modulo OS
# help('os')

# 2 - Retornar a pasta atual
print(os.getcwd())

# 3 - Listar arquivos e pastas
print(os.listdir())

# 4 - Apresentar a versão do SO
os.system('ver')

# 5 - Configurações da maquina
os.system('systeminfo')

# 6 - Limpar a tela do terminal
os.system('cls')

