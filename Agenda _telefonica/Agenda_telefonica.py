'''

Uma agenda telefônica feita com python e CSV
Autor: José Henrique

A phone book made with python and CSV
Author: José Henrique

'''



from tkinter import ttk
from tkinter.ttk import *
from tkinter import*

from tkinter import messagebox

from dados import *

import sys
import csv


# Colors -----------------------------------------------------

co0 = "#f0f3f5"  # black
co1 = "#f0f3f5"  # grey
co2 = "#feffff"  # white
co3 = "#38576b"  # black
co4 = "#403d3d"   # letra
co5 = "#6f9fbd"  # blue
co6 = "#ef5350"   # red
co7 = "#93cd95"   # green


# Creating the window ----------------------------------------

janela = Tk ()
janela.title ("")
janela.geometry('500x450')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames ------------------------------------------------------

frames_cima = Frame(janela, width=500, height=50,bg=co5, relief="flat")
frames_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frames_baixo = Frame(janela, width=500, height=150,bg=co1, relief="flat")
frames_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frames_tabela = Frame(janela, width=500, height=248,bg=co2, relief="flat")
frames_tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)


#Settings Frame Cima

l_nome = Label(frames_cima, text='Lista Telefonica', anchor=NE, font=('times 23 bold'), bg=co5, fg=co1)
l_nome.place(x=5, y=2.5)

l_linha = Label(frames_cima, text='',width=500, anchor=NE, font=('times 1'), bg=co2, fg=co1)
l_linha.place(x=0, y=46)



global tree
#Frame Table Configuration ----------------------------------
def mostrar_dados():

    global tree
    # creating a treeview with dual scrollbars

    dados_h = ['Nome', 'Sexo', 'telefone', 'email']

    dados = ver_dados()



    tree = ttk.Treeview(frames_tabela, selectmode="extended", columns=dados_h, show="headings")

    # vertical scrollbar

    vsb = ttk.Scrollbar(frames_tabela, orient="vertical", command=tree.yview)

    # Horizontal scrollbar

    hsb = ttk.Scrollbar(frames_tabela, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')


    # tree heading

    tree.heading(0,text='Nome', anchor=NW)
    tree.heading(1,text='Sexo', anchor=NW)
    tree.heading(2,text='Telefone', anchor=NW)
    tree.heading(3,text='E-mail', anchor=NW)

    #tree body

    tree.column(0, width=120,anchor='nw')
    tree.column(1, width=50,anchor='nw')
    tree.column(2, width=100,anchor='nw')
    tree.column(0, width=120,anchor="nw")


    for item in dados:
        tree.insert('', 'end', values=item)



mostrar_dados()



# function inset

def inserir():
    nome = e_nome.get()
    sexo = c_sexo.get()
    telefone = e_tel.get()
    email = e_email.get()

    dados = [nome, sexo, telefone, email]

    if nome == '' or sexo == '' or telefone == '' or email == '':
        messagebox.showwarning('Dados', 'Por favor preencha todos os campos')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'Dados adicionados com sucesso')

        e_nome.delete(0,'end')
        c_sexo.delete(0,'end')
        e_tel.delete(0,'end')
        e_email.delete(0,'end')


        mostrar_dados()



def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        nome = tree_lista[0]
        sexo = tree_lista[1]
        telefone =str(tree_lista[2])
        email = tree_lista[3]

        e_nome.insert(0,nome)
        c_sexo.insert(0,sexo)
        e_tel.insert(0,telefone)
        e_email.insert(0,email)


        
        def confirmar():

            nome = e_nome.get()
            sexo = c_sexo.get()
            telefone_novo = e_tel.get()
            email = e_email.get()

            dados = [telefone,nome, sexo, telefone_novo, email]

            print(dados)

            atualizar_dados(dados)

        
            messagebox.showinfo('Dados', 'Dados atualizados com sucesso')

            e_nome.delete(0,'end')
            c_sexo.delete(0,'end')
            e_tel.delete(0,'end')
            e_email.delete(0,'end')

            b_confirmar.destroy()

            mostrar_dados()

        b_confirmar = Button(frames_baixo, command=confirmar, text='Confirmar ', width=10, font=('ivy 8 bold '), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290, y=110)      
    except: 
        messagebox.showwarning('Dados', 'Por favor selecione uma informação na tabela')



def remover():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        telefone = str(tree_lista[2])

        remover_dados(telefone)

        messagebox.showinfo('Dados', 'Dados removidos com sucesso')

        for widget in frames_tabela.winfo_children():
            widget.destroy()

        mostrar_dados()



    except: 
        messagebox.showwarning('Dados', 'Por favor selecione uma informação na tabela')



def buscar():
    telefone = e_procurar.get()

    dados = pesquisar_dados(telefone)

    tree.delete(*tree.get_children())

    for item in dados:
        tree.insert('', 'end', values=item)

    e_procurar.delete(0,'end')


#Settings Frame Baixo

l_nome = Label(frames_baixo, text='Nome *', anchor=NW, font=('ivy 10 '), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frames_baixo, width=25,justify='left',relief=FLAT, font=('',10), highlightthickness=1)
e_nome.place(x=80, y=20)

l_sexo = Label(frames_baixo, text='Sexo *', anchor=NW, font=('ivy 10 '), bg=co1, fg=co4)
l_sexo.place(x=10, y=50)
c_sexo = Combobox(frames_baixo, width=27)
c_sexo['value'] = ('', 'F', 'M' )
c_sexo.place(x=80, y=50)

l_tel = Label(frames_baixo, text='Telefone *', anchor=NW, font=('ivy 10 '), bg=co1, fg=co4)
l_tel.place(x=10, y=80)
e_tel = Entry(frames_baixo, width=25,justify='left',relief=FLAT, font=('',10), highlightthickness=1)
e_tel.place(x=80, y=80)

l_email = Label(frames_baixo, text='E-mail *', anchor=NW, font=('ivy 10 '), bg=co1, fg=co4)
l_email.place(x=10, y=110)
e_email = Entry(frames_baixo, width=25,justify='left',relief=FLAT, font=('',10), highlightthickness=1)
e_email.place(x=80, y=110)

#Buttons

b_procurar = Button(frames_baixo, command=buscar, text='Buscar ', font=('ivy 8 bold '), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_procurar.place(x=290, y=20)
e_procurar = Entry(frames_baixo, width=16,justify='left',relief=FLAT, font=('',11), highlightthickness=1)
e_procurar.place(x=347, y=21)


b_ver = Button(frames_baixo, command=mostrar_dados, text='Ver dados ', width=10, font=('ivy 8 bold '), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_ver.place(x=290, y=50)

b_adicionar = Button(frames_baixo, command=inserir, text='Adicionar ', width=10, font=('ivy 8 bold '), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_adicionar.place(x=400, y=50)

b_atualizar = Button(frames_baixo,command=atualizar, text='Modificar ', width=10, font=('ivy 8 bold '), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=400, y=80)

b_deletar = Button(frames_baixo,command=remover, text='Remover ', width=10, font=('ivy 8 bold '), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=400, y=110)




janela.mainloop()
