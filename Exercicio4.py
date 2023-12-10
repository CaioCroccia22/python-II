"""
Adivinhe o Número 
-> Escreva um programa em python que gera um numero aleatorio para que o 
usuário tente acertar o número. Algumas sugestões para o programa:

1 - Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente a opção para sair do programa.

2 - Utilizar o modulo random para gerar valores aleatorios dentro de um intervalo. ex: 1 a 10

3 - Le o numero que o usuario digitar via input e comparar se é o mesmo número que o programa sorteou 

"""
import random

number = int

def get_number():
    list_number = [random.randint(1, 100) for i in range(5)]
    print(list_number)
    for i in list_number:
        number = random.choice(list_number)
        print(number)
        number_user = int(input("Digite o número que voce pensa que é: \n"))
        print(number)
        if number == number_user:
            print("Parabens voce acertou o número!!")
        
        
get_number()