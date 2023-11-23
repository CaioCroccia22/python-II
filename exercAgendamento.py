"""
Agendamento de desligamento em python
-> Crie duas funções em python para agendar o desligamento do 
computador em uma hora.
"""

import os


shutdown = input("Deseja desligar o computador? (sim/não):")

def shutdown_computer():
    if shutdown == 'sim':
        os.system("shutdown /s /t 3600")
    if shutdown == 'não':
        exit()

shutdown_computer()

def cancel_shutdown():
    if shutdown == 'sim':
        os.system("shutdown /a")

cancel_shutdown()



# #Desligar o computador em 1 minuto
# os.system("shutdown /s") 

# #Desligar o computador agora
# os.system("shutdown /s /t 0")

# #Cancelar o desligamento
# os.system("shutdown /a")