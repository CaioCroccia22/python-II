"""
Agendamento de desligamento em python
-> Crie duas funções em python para agendar o desligamento do 
computador em uma hora e meia hora.
"""

import os


shutdown = input("Deseja desligar o computador? (sim/não):")

def shutdown_computer():
    if shutdown == 'sim':
        os.system("shutdown /s /t 1")
    if shutdown == 'não':
        exit()

shutdown_computer()