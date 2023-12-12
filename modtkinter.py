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
frase_lab = tkinter.Label()

window.mainloop()

