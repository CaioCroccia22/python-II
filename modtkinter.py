import builtins
import tkinter
 
# 1 - Criando a janela
window = tkinter.Tk()
window.geometry("300x150")
window.title("Gerenciador de frases")


# 2 - Adicionando o Frame
frame = tkinter.Frame(window)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# 3 - Adicionando o label
label = tkinter.Label(frame, text="Hello World!!")
label.pack(fill='x', expand=True)

# 4 - Adicionando o input text
frase_lab = tkinter.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)


frase_inp = tkinter.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - Adicionar a função para alterar o texto do label
def click():
    label.config(text=frase_inp.get())




# 6 - Adicionando o botão 
button = tkinter.Button(frame, text="Enviar", command=click)
button.pack()


window.mainloop()

