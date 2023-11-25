import webbrowser

done = False


while done == False:
    print("O que você deseja fazer?")
    print("1. Aprender Python")
    print("2. Aprender sobre módulos")
    print("3. Aprender Python, fullstack JS, Ingles e No Code")
    print("4. Sair")

    choices = input("> ")
    if choices == "1":
        webbrowser.open("http://www.python.org")
    if choices == "2":
        webbrowser.open("https://docs.python.org/3/py-moindex.html")
    if choices == "3":
        webbrowser.open("https://pages.onebitcode.com/")
    if choices == "4":
        done = True
    else:
        print("Escolha uma opção válida entre 1 e 4")
    


    