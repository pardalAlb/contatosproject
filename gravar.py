import os
import csv
import tkinter as tk
from tkinter import messagebox

def gravar_contato():
   if entry_nome.get() == "" or entry_telefone.get() == "" or entry_email.get() == "":
      messagebox.showerror("Erro ao gravar", "Todos os campos devem estar preenchidos")

   else:
        with open("dados.csv", "a", newline="") as arquivo_dados:
            escritor = csv.writer(arquivo_dados)
            escritor.writerow([entry_nome.get(), entry_telefone.get(), entry_email.get().strip()])
            messagebox.showinfo("Sistema contatos", "Contato cadastrado com êxito!")
            limpar_campos()
            entry_nome.focus_set()
        ler_contatos()


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_nome.focus_set()
def ler_contatos():
    with open("dados.csv", "r") as arquivo_dados:
        leitor = csv.reader(arquivo_dados)
        label_contatos.delete(0, tk.END)
        for linha in leitor:
            label_contatos.insert("end", linha[0])

def buscar_contato_pelo_indice(indice_procurado):
    with open("dados.csv", "r") as arquivo_dados:
        leitor = csv.reader(arquivo_dados)
        for linha in leitor:
            if volta == indice_procurado:
                entry_nome.insert(tk.END, linha[0])
                entry_telefone.insert(tk.END, linha[1])
                entry_email.insert(tk.END, linha[2])
                break
            volta = volta + 1
def obter_indice(event):
    indice = label_contatos.curselection()[0]
    limpar_campos()
    buscar_contato_pelo_indice(indice)


def apagar_contato(linha):
   resposta = messagebox.askokcancel("Excluir contato", "Tem certeza que deseja excluir o contato selecionado?")

   if resposta:
        with open("dados.csv", "r") as arquivo_dados, open("temp.csv", "a") as arquivo_temp:
            leitor = csv.reader(arquivo_dados)
            escritor = csv.writter(arquivo_temp)

            for contato in leitor:
                if entry_nome.get() != contato[0] and entry_telefone.get() != contato[1] and entry_email.get() != contato[2]:
                    escritor.writerow([contato[0], contato[1], contato[2]])
        os.remove("dados.csv")
        os.rename("temp.csv", "dados.csv")
        limpar_campos()
        ler_contatos()
   else:
        messagebox.showinfo("Excluir contato", "Operação cancelada pelo usuário.")


indice = 0

janela = tk.Tk()

janela.geometry("580x300")

label_nome = tk.Label(janela, text="Nome")
label_telefone = tk.Label(janela, text="Telefone")
label_email = tk.Label(janela, text="E-mail")
label_contatos = tk.Label(janela, text="Contatos")

entry_nome = tk.Entry(janela)
entry_telefone = tk.Entry(janela)
entry_email = tk.Entry(janela)

button_gravar = tk.Button(text= "Salvar", command=gravar_contato)
button_gravar.place(x=10, y=230, width=150, height=60)
button_excluir = tk.Button(text="Excluir", command=apagar_contato())
button_excluir.place(x=165, y=230, width=150, height=60)

label_contatos = tk.Listbox(janela, selectmode="single")
label_contatos.bind("<<ListboxSelect>>", obter_indice)

label_nome.config(font=("Consolas", 15))
label_nome.place(x=10, y=10)
entry_nome.config(font=("Consolas", 16))
entry_nome.place(x=10, y=40, width=300, height=30)

label_telefone.config(font=("Consolas", 16))
label_telefone.place(x=10, y=80)
entry_telefone.config(font=("Consolas", 16))
entry_telefone.place(x=10, y=110, width=300, height=30)

label_email.config(font=("Consolas", 15))
label_email.place(x=10, y=150)
entry_email.config(font=("Consolas", 15))
entry_email.place(x=10, y=180, width=300, height=30)

button_gravar.config(font=("Consolas", 16))
button_excluir.config(font=("Consolas", 16))


label_contatos.config(font=("Consolas", 16))
label_contatos.place(x=320, y=40, width=250)

ler_contatos()

janela.mainloop()


nome = input("Informe seu nome: ")
telefone = input("Informe seu telefone: ")
email = input("Informe seu email: ")
