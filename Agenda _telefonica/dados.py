#import CSV
import csv

lista = ['Jose', 'M', '1234567', 'Jose@gmail.com' ]

#function add
def adicionar_dados(i):
    # Accessing CSV
    with open('dados.csv', 'a+', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)

    



# View data function
    
def ver_dados():
    dados = []
    # Accessing CSV
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            dados.append(linha)
    return dados


# remove data function
def remover_dados(i):
    def adicionar_novalista(j):
        # Accessing CSV
        with open('dados.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
            ver_dados()
        
            

    nova_lista = []
    telefone = i
    with open('dados.csv', 'r') as file:
        ler_csv = csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nova_lista.remove(linha)

    #add new list           
    adicionar_novalista(nova_lista)





# update data function
def atualizar_dados(i):
    def adicionar_novalista(j):
        # Accessing CSV
        with open('dados.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
            ver_dados()
        
            

    nova_lista = []
    telefone = i[0]
    with open('dados.csv', 'r') as file:
        ler_csv = csv.reader(file)

        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == telefone:
                    nome = i[1]
                    sexo = i[2]
                    tel = i[3]
                    email = i[4]

                    dados = [nome, sexo, tel, email]

                     #Swapping list for index
                    index = nova_lista.index(linha)
                    nova_lista[index] = dados

   

    #add new list           
    adicionar_novalista(nova_lista)



# Search Data Function

def pesquisar_dados(i):
    dados = []
    telefone = i

    print(i)

    # Accessing CSV
    with open('dados.csv') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            for campo in linha:
                if campo == telefone:
                    dados.append(linha)
    return dados



    
