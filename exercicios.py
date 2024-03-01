# 1) Em muitos programas, nos é solicitado o preenchimento de algumas informações como
# nome, CPF, idade e unidade federativa. Escreva um script em Python que solicite as
# informações cadastrais mencionadas e que em seguida as apresente da seguinte forma:

# -----------------------------
# Confirmação de cadastro:
# Nome: Guido Van Rossum
# CPF: 999.888.777/66
# Idade: 65
# -----------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@ RESULTADO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# print("Confirmação de cadastro")
# nome = input("Nome: ")
# cpf = input("CPF: ")
# idade = input("Idade: ")

# print("Seja Bem vindo "+ nome +". Cadastro confirmado.")
# print(nome)
# print(cpf)
# print(idade)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # 2) Escreva um script em Python que receba dois números e que seja realizado as seguintes
# # operações:
# # • soma dos dois números
# # • diferença dos dois números
# # O resultado deverá ser apresentado conforme a seguir - no exemplo foram digitados os números
# # 4 e 2:

# # ------------------------------
# # Soma: 4 + 2 = 6
# # Diferença: 4 - 2 = 2

#@@@@@@@@@@@@@@@@@@@@@@ RESULTADO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# a = int(input("Digite o primeiro numero: "))
# b = int(input("Digite o segundo numero: "))
# soma = a+b
# sub = a-b


# print("Soma ",a," + ",b," = ",soma)
# print("Diferença ",a," - ",b," = ",sub)

# #Só um outro jeito de fazer esse print pra testar
# print("Soma " + str(a) + " + " + str(b) + " = " + str(soma) )
# print("Diferença " + str(a) + " - " + str(b) +" = " + str(sub) )

#Exercicio salvo : https://gitlab.com/study4034308/python-4linux/-/blob/main/aula01.py?ref_type=heads
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#########################################################################################################

# 1) Escreva um script em Python que substitua o caractere “x” por espaço considerando a
# seguinte frase:“Umxpratoxdextrigoxparaxtrêsxtigresxtristes”

#@@@@@@@@@@@@@@@@@@@@@@@@@@@ RESULTADO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# output=""
# input = "Umxpratoxdextrigoxparaxtrêsxtigresxtristes"
# for i in input:
#     if i == "x":
#         i = " "
#         output = output+i
#     else:
#         output = output+i
# print(output)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ======================================================================================================
# 2) Escreva um programa que receba o ano de nascimento, e que ele retorne à geração
# a qual a pessoa pertence. Para definir a qual geração uma pessoa pertence temos a
# seguinte tabela:

# Geração        Intervalo

# Baby Boomer -> Até 1964
# Geração X   -> 1965 - 1979
# Geração Y   -> 1980 - 1994
# Geração Z   -> 1995 - Atual

# Para testar se seu script está funcionando, considere os seguintes resultados esperados:

# • ano nascimento = 1988: Geração: Y
# • ano nascimento = 1958: Geração: Baby Boomer
# • ano nascimento = 1996: Geração: Z

#@@@@@@@@@@@@@@@@@@@@@@@@@@@ RESULTADO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ano = int(input('Ano nascimento:'))
# if ano <= 1964:
#     r = "Baby Boomer"
# elif ano <= 1979:
#     r = "Geração X"
# elif ano <= 1994:
#     r = "Geração Y"
# else:
#     r = "Geração Z"

# print(r)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ======================================================================================================
# 3) Escreva um script em python que represente uma quitanda. O seu programa deverá
# apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
# deverá ser adicionada a uma cesta de compras.

# Menu principal:

# Quitanda:
# 1: Ver cesta
# 2: Adicionar frutas
# 3: Sair

# Menu de frutas:
# Digite a opção desejada:
# 1 - Banana
# 2 - Melancia
# 3 - Morango

# Os menus 1 e 2 deverão retornar ao menu principal após executar as suas tarefas.
# Você deverá validar as opções digitadas pelo usuário (caso ele digitar algo errado, a mensagem:
# Digitado uma opção inválida

# O programa deverá ser encerrado apenas se o usuário digitar a opção 3.

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ RESULTADO @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# option=0
# cesta=[]
# while (option != 3):
#     print("""Quitanda:
#         # 1: Ver cesta
#         # 2: Adicionar frutas
#         # 3: Sair """ )
#     option = int(input("Qual opção deseja?"))
#     if option == 1:
#         print(cesta)
#     elif option == 2:
#         print("""Menu de Frutas
#         #Digite a opção desejada:
#         # 1: Banana
#         # 2: Melancia
#         # 3: Morango """ )
#         fruta = int(input("Opção: "))
#         if fruta == 1:
#             cesta.append("Banana")
#         elif fruta == 2:
#             cesta.append("Melancia")
#         elif fruta == 3:
#             cesta.append("Morango")
#         else:
#             print("Opção Inválida")
#     elif option > 3:
#         print("Você digitou opção errada")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ RESULTADO PROFESSOR @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@ TRATAMENTO MELHOR DE ERROS E LIMPESA DO TERMINAL
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# cesta = []

# while True:
#     resposta = input("""
# Quitanda:
# 1: Ver cesta
# 2: Adicionar frutas
# 3: Sair
# """)

#     if resposta == "1":

#         if os.name == "posix":
#             os.system("clear")
#         else:
#             os.system("cls")

#         if len(cesta) == 0:
#             print("Sua cesta ainda está vazia")
#         else:
#             print(f"A sua cesta atualmente possui: {cesta}")

#     elif resposta == "2":

#         if os.name == "posix":
#             os.system("clear")
#         else:
#             os.system("cls")

#         fruta = input(
# """Escolha uma fruta:
# 1 - Banana
# 2 - Melancia
# 3 - Morango
# """)
#         if fruta == "1":
#             print("Adicionando uma banana à cesta")
#             cesta.append("Banana")
#         elif fruta == "2":
#             print("Adicionando uma melancia à cesta")
#             cesta.append("Melancia")
#         elif fruta == "3":
#             print("Adicionando um morango à cesta")
#             cesta.append("Morango")
#         else:
#             print("Voce digitou um valor invalido")
    
#     elif resposta == "3":

#         if os.name == "posix": # Linux
#             os.system("clear")
#         else:                  # NT = Windows
#             os.system("cls") 

#         print("Parando o programa...")
#         break

#     else:
#         print("Voce digitou um valor invalido")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@ AULA 04 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Exercicio 1:
# Escreva uma função que receba um nome e que tenha como saída uma saudação.
# O argumento da função deverá ser o nome, e saída deverá ser como a seguir:
# chamada da função: saudacao('Lalo')
# saída: 'Olá Lalo! Tudo bem com você?'

# def greet(name):
#     print(f"Ola {name}! Tudo bem com você? ")

# n = input("Name: ")
# greet(n)
#=======================================================================
#Using Lambda
#=======================================================================
# n = input("Name: ")
# greet = lambda name: print(f"Ola {name}! Tudo bem com você? ")
# print(greet(n))
# ====================================================
# Exercicio 2:
# Escreva uma calculadora utilizando funções
# Ela pergunta dois numeros, e da as opções de calculo.
# (soma, diferença, multiplicação, divisão)
# ops = " "
# num = []

# def check():
#     if ops == 1:
#         soma(num[0],num[1])

#     if ops == 2:
#         sub(num[0],num[1])

#     if ops == 3:
#         mult(num[0],num[1])

#     if ops == 4:
#         div(num[0],num[1])
#     return ops

# def soma(a,b):
#     result= a + b
#     print(f"A soma de {a} + {b} = {result}")

# def sub(a,b):
#     result= a - b
#     print(f"A subtração de {a} - {b} = {result}")

# def mult(a,b):
#     result= a * b
#     print(f"A multiplicação de {a} * {b} = {result}")

# def div(a,b):
#     result= a / b
#     print(f"A divisão de {a} / {b} = {result}")



# while len(num)<2:
#     num.append(int(input("Digite DOIS números: ")))

# while ops != 1 and ops != 2 and ops != 3 and ops != 4:
#     ops = int(input(""" ---- OPERAÇÃO ----
#         #1 - SOMA
#         #2 - SUBTRAÇÃO
#         #3 - MULTIPLICAÇÃO
#         #4 - DIVISÃO      
#     """))

# check()
# ====================================================
# Exercicio 3:
# Escreva um programa que possua uma função que conte o
# numero de números pares passados à ela, pelo usuário.
# res=0
# num = range(0,101)
# for i in num:
#     if i % 2 == 0:
#         res= res+1
#     print(i)
# print(f"Existem {res} número pares no universo de {num}")
# ====================================================
# Exercicio 4:
# Reescreva o exercício da quitanda do capítulo 2 separando as operações
# em funções, e adiconando um preço para cada fruta, de modo que quando a pessoa
# fizer o checkout ela consiga ver o preço total a pagar.

# option=0
# total=0
# cesta=[]
# catalogo={"Banana":8.00,"Melancia":20.00,"Morango":5.00}

# def showcesta(a,b):
#     print(f"Os itens selecionados foram {a}")
#     print(f"O total das suas compras ficaram: {b}")

# def additem():
#     global total #Teoricamente não precisaria desse "global", mas a execução reclamou de não conseguir acessar a var total, essa declaração acertou isso.
#     print(f"""Menu de Frutas
#         #Digite a opção desejada:
#         # 1: Banana - {catalogo["Banana"]}
#         # 2: Melancia - {catalogo["Melancia"]}
#         # 3: Morango - {catalogo["Morango"]} """ )
#     fruta = int(input("Opção: "))
#     if fruta == 1:
#         cesta.append("Banana")
#         total=total+catalogo["Banana"]
#     elif fruta == 2:
#         cesta.append("Melancia")
#         total=total+catalogo["Melancia"]
#     elif fruta == 3:
#         cesta.append("Morango")
#         total=total+catalogo["Morango"]
#     else:
#         print("Opção Inválida")


# while (option != 3):
#     print("""Quitanda:
#         # 1: Ver cesta
#         # 2: Adicionar frutas
#         # 3: Sair """ )
#     option = int(input("Qual opção deseja?"))
#     if option == 1:
#         showcesta(cesta,total)
#     elif option == 2:
#         additem()
#     elif option > 3:
#         print("Você digitou opção errada")

# 1) Escreva um programa em Python que simule uma dança das cadeiras. Você deverá
# importar o pacote random e iniciar uma lista com nomes de pessoas que participariam da
# brincadeira. O jogo deverá iniciar com 9 cadeiras e 10 participantes. A cada rodada,
# uma cadeira deverá ser retirada e um dos jogadores, de forma aleatória, ser eliminado. O
# jogo deverá terminar quando apenas restar uma cadeira e ao final de todas as rodadas,
# deverá ser apresentado vencedor.

# Dica: [OPCIONAL] Você poderá utilizar o modulo "time" para simular um tempo de a cada rodada para criar
# um efeito mais interessante.

# Dica: [OPCIONAL] Tentem fazer a remoção de uma pessoa aleatória por rodada sem utilizar a função "choice".

# import random
# import time

# participantes = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", "Rosangela", "Rian"]
# # # INDEX             0       1        2         3         4          5        6        7            8        9

# wait = 3 #3 seconds 


# print(participantes)
# print(len(participantes))

# while len(participantes) > 1:
#     cadeira = random.randrange(0,len(participantes))
#     participantes.pop(cadeira)
#     print(participantes)
#     time.sleep(wait)
    
# print(f"Vencedor: {participantes}")

# ===========================================================================================
# 2) Escreva um programa em python que conte as vogais que a música ‘Faroeste Caboclo’
# tem em sua letra. Armazena a letra da música em um arquivo do tipo txt.
# Dica: Não se esqueça de considerar as letras maiúsculas, minúsculas e com acentuação.

# def count_v(texto):
    
#     vogais = "aeiouAEIOUáéíóúâêîôûàã"
#     count = 0

#     for i in texto:
#         lowercase = i.lower()
#         if lowercase in vogais:
#             count = count+1
#     print(f"Há {count} vogais no raio da música, Faroeste Caboclo")

# with open("faroeste.txt","r" ) as file:
#     conteudo = file.read() 
#     print(conteudo) #Só imprimindo para verificar a letra da música e garantir que não deu erro de Coding
#     count_v(conteudo)


# ======================================================================================================
# ======================================================================================================
# 1) Crie uma classe que represente um ônibus. O ônibus deverá conter os seguintes atributos:

# capacidade total
# capacidade atual
# movimento

# Os comportamentos esperados para um Ônibus são:
# Embarcar
# Desembarcar
# Acelerar
# Frear

# Lembre-se que a capacidade total do ônibus é de 45 pessoas - não será possível admitir super-
# lotação. Além disso, quando o ônibus ficar vazio, não será permitido efetuar o desembarque
# de pessoas. Além disso, pessoas não podem embarcar ou desembarcar com o onibus em movimento.

# class Onibus:

#     def __init__(self,cap=45):
#         self.capacidade_total = cap
#         self.capacidade_atual = 0
#         self.movimento = False
    
#     def acelerar(self):
#         self.movimento = True
#         return ("Onibus acelerado")

    
#     def frear(self):
#         if self.movimento == True:
#             self.movimento = False
#             return (f"Onibus parado. Pronto para embarcar")
#         else:
#             return ("O ônibus já está parado")
    
#     def embarcar(self, qtd=1):
#         if self.movimento == False:
#             if self.capacidade_atual < 45:
#                 if self.capacidade_atual + qtd <= self.capacidade_total:
#                         self.capacidade_atual = self.capacidade_atual + qtd
#                         return (f"A capacidade atual no ônibus é: {self.capacidade_atual}")
#                 else:
#                     return(f"Você está tentando embarcar gente demais.")
#             else:
#                 return ("O ônibus já está na sua capacidade máxima !")
#         else:
#             return ("O onibus está em movimento. Você precisa parar primeiro")

#     def desembarcar(self, qtd=1):
#         if self.movimento == False:
#             if self.capacidade_atual > 0:
#                 self.capacidade_atual = self.capacidade_atual - qtd
#                 return (f"A capacidade atual no ônibus é: {self.capacidade_atual}")
#             else:
#                 return (f"Se o onibus está vazio. Quem puxou a cordinha ????")
#         else:
#             return (f"O onibus está em movimento. Você precisa parar primeiro")
# meu_onibus = Onibus()



# print(meu_onibus.embarcar(44))
# print(meu_onibus.embarcar(5))

# print(meu_onibus.acelerar())
# print(meu_onibus.embarcar(10))
# print(meu_onibus.desembarcar(10))

# print(meu_onibus.frear())
# print(meu_onibus.embarcar(10))

# print(meu_onibus.desembarcar(40))
# print(meu_onibus.acelerar())
# print(meu_onibus.desembarcar(3))

# ==========================================================================
# 2) Implemente um programa que represente uma fila. O contexto do programa é uma
# agência de banco. Cada cliente ao chegar deverá respeitar a seguinte regra: o primeiro
# a chegar deverá ser o primeiro a sair. Você poderá representar pessoas na fila a par-
# tir de números os quais representam a idade. A sua fila deverá conter os seguintes
# comportamentos:

# • Adicionar pessoa na fila: adicionar uma pessoa na fila.
# • Atender Fila: atender a pessoa respeitando a ordem de chegada
# • Dar prioridade: colocar uma pessoa maior de 65 anos como o primeiro da fila

# class Fila:

#     def __init__(self):
#         self.fila = []
#         self.idade = 0
#         self.qtd = 0
        
#     def add(self,age):
#         self.idade = age
#         self.qtd += 1
#         self.fila.append(self.idade)
#         return (f"A fila tem {self.qtd} pessoas - \n {self.fila}")
    
#     def attend(self):
#         self.qtd -= 1
#         self.fila.pop(0)
#         return (f"A fila agora tem {self.qtd} pessoas. {self.fila}")
    
#     def prior(self,age=65):
#         for x in self.fila:
#             if x >= age:
#                 oldest = max(self.fila) #Achando o maior valor da lista com a função max
#                 i = self.fila.index(oldest) #Atribuindo o valor do index desse maior valor à variável i         
#                 self.fila.pop(i)
#                 self.fila.insert(0, oldest) #Inserindo no index 0 o valor maior encontrado, representando a pessoa mais velha
#                 return (f"Reordenando a fila por prioridade \n Acima de {age} anos \n Mais velho a frente \n -> {self.fila}")
#         return(f"Não tem ninguém acima de 65 anos na fila")

# fila_banco = Fila()

# print(fila_banco.add(45))
# print(fila_banco.add(43))
# print(fila_banco.add(60))
# print(fila_banco.add(42))
# print(fila_banco.add(80))

# print(fila_banco.prior())
# print(fila_banco.attend())
# print(fila_banco.prior(60)) #Alterando idade prioritária
# print(fila_banco.attend())
# print(fila_banco.prior())
# print(fila_banco.attend())

# Crie um script para simular uma lanchonete.
# 
# - Essa lanchonete deverá ter 5 tipos de comida e 3 tipos de bebidas no cardápio.
# - Quando clientes chegarem a essa lanchonete, eles deverão fazer um pedido aleatório de comida + bebida.
# - A lanchonete deverá ter um numero limitado de porções dessas comidas/bebidas. Comida = 5, bebida = 7.
# - Quando o cliente fazer o pedido, ele deverá ser notificado se as opções escolhidas estão disponiveis,
# e quais seus preços.

# Criar um DB.
# Criar uma tabela pra comida e uma pra bebida.
# Preencher essas tabelas.

# Criar uma função pra simular um cliente comprando algo.

###################################################################################################

#########################################  MINHA SOLUCAO #########################################
###################################################################################################


# import sqlite3

# limite_tipo_comida = 5
# limite_tipo_bebida = 3
# limite_qtde_comida = 5
# limite_qtde_bebida = 7


# def criar_base(tablecomida="comida",tablebebida="bebida"):
#     conexao = sqlite3.connect(f"lanchonete.db")  # Cria ou se conecta a um banco de dados existente.
#     cursor = conexao.cursor()  
#     cria_comida = f"""
#     CREATE TABLE {tablecomida} (
#     id integer primary key autoincrement, 
#     produto text, 
#     quantidade integer,
#     preco real
#     )"""
#     cria_bebida = f"""
#     CREATE TABLE {tablebebida} (
#     id integer primary key autoincrement, 
#     produto text, 
#     quantidade integer,
#     preco real
#     )"""
#     try:
#         cursor.execute(cria_comida)              
#         cursor.execute(cria_bebida)        
#         print(f"DB lanchonete.db criado")
#         print(f"Tabelas {tablecomida} & {tablebebida} criadas")
#     except sqlite3.OperationalError: #Caso de erro na criação da tabela por já existir ele passa
#         pass

#     conexao.commit()    
#     conexao.close()

# def register_prod(table,prod,qtde=0,price=0):
#     if table == "comida":
#         if qtde > limite_qtde_comida:
#             print(f"Não é possível adicionar essa quantidade de {prod} de comida")
#         else:
#             if len((consulta_tabela(f"{table}"))) == limite_tipo_comida:
#                 print("Número máximo de comida no estoque atingido")
#             else:
#                 conexao = sqlite3.connect("lanchonete.db")  # Cria ou se conecta a um banco de dados existente.
#                 cursor = conexao.cursor()  
#                 adiciona_prod = f"""
#                 INSERT INTO {table} (produto,quantidade,preco)
#                 VALUES ("{prod}",{qtde}, {price})"""
#                 print(f"{prod} registrado na tabela {table}")
#                 cursor.execute(adiciona_prod)              
#                 conexao.commit()    
#                 conexao.close()
#     if table == "bebida":
#         if qtde > limite_qtde_bebida:
#             print("Não é possível adicionar essa quantidade de bebidas")
#         else:
#             if len((consulta_tabela(f"{table}"))) == limite_tipo_bebida:
#                 print("Número máximo de bebida no estoque atingido")
#             else:
#                 conexao = sqlite3.connect("lanchonete.db")  # Cria ou se conecta a um banco de dados existente.
#                 cursor = conexao.cursor()  
#                 adiciona_prod = f"""
#                 INSERT INTO {table} (produto,quantidade,preco)
#                 VALUES ("{prod}",{qtde}, {price})"""
#                 print(f"{prod} registrado na tabela {table}")
#                 cursor.execute(adiciona_prod)              
#                 conexao.commit()    
#                 conexao.close()

# def consulta_tabela(table):
#     conexao = sqlite3.connect("lanchonete.db")  # Cria ou se conecta a um banco de dados existente.
#     cursor = conexao.cursor()  
#     checa_tabela = f"SELECT * FROM {table}"
#     cursor.execute(checa_tabela)              

#     select_table = cursor.fetchall()
#     print(select_table)
#     conexao.close()
#     return select_table

# def consulta_produtos(table):
#     nome_prod = []
#     conexao = sqlite3.connect("lanchonete.db")  # Cria ou se conecta a um banco de dados existente.
#     cursor = conexao.cursor()  
#     checa_prods = f"SELECT produto FROM {table}"
#     cursor.execute(checa_prods)              
#     select_prods = cursor.fetchall()
#     conexao.close()
#     for i in select_prods:
#         nome_prod.append(str(i[0]))
#     return nome_prod

# def consulta_qtde(table,prod):
#     conexao = sqlite3.connect("lanchonete.db")  # Cria ou se conecta a um banco de dados existente.
#     cursor = conexao.cursor()  
#     checa_qtde = f'SELECT quantidade FROM {table} WHERE produto = "{prod}"'
#     cursor.execute(checa_qtde)              

#     select_qtde = cursor.fetchall()
#     conexao.close()
#     # print("AQUI !", select_qtde)
#     for i in select_qtde:
#         qtde_int = int(i[0])
#     return qtde_int

# def consulta_preco(table,prod):
#     conexao = sqlite3.connect("lanchonete.db")  # Cria ou se conecta a um banco de dados existente.
#     cursor = conexao.cursor()  
#     checa_preco = f'SELECT preco FROM {table} WHERE produto = "{prod}"'
#     cursor.execute(checa_preco)              

#     select_preco = cursor.fetchall()
#     conexao.close()
#     for i in select_preco:
#         preco_float = float(i[0])
#     return f"{preco_float}"

# def alterar_qtde(table,prod,q=0):
#     conexao = sqlite3.connect("lanchonete.db")  # Cria ou se conecta a um banco de dados existente.
#     cursor = conexao.cursor()  
#     altera_qtde = f'UPDATE {table} SET quantidade = {q} WHERE produto = "{prod}"'
#     cursor.execute(altera_qtde)
#     conexao.commit()
#     conexao.close()

# def alterar_preco(table,prod,p=0):
#     conexao = sqlite3.connect("lanchonete.db")  # Cria ou se conecta a um banco de dados existente.
#     cursor = conexao.cursor()  
#     alter_preco = f'UPDATE {table} SET preco = {p} WHERE produto = "{prod}"'
#     cursor.execute(alter_preco)
#     conexao.commit()
#     conexao.close()

# def fazer_pedido(table,*itens): #This *itens allows multiple arguments to the iten parameter in the function
#     preco_comida = []
#     preco_aux = 0.00
#     for i in itens:
#         produtos_cadastrados = consulta_produtos(f"{table}")
#         if i not in produtos_cadastrados:
#             print(f"Produto não cadastrado. Ainda não temos {i} na lista de produtos")
#             continue
#         else:
#             quantidade_estoque = consulta_qtde(table,i)
#             if quantidade_estoque == 0:
#                 print(f"Não temos mais {i}")
#             else:
#                 nova_quantidade = quantidade_estoque - 1
#                 alterar_qtde(table,i,nova_quantidade)
#                 preco_comida.append(float(consulta_preco(table, i)))
#                 for n in preco_comida:
#                     preco_aux = preco_aux + n
#     print(f"O valor da sua conta = {preco_aux}")

# #Criando a base
# criar_base()

# #Registrando os produtos
# # register_prod("comida","xsalada", 2, 5.50)
# # register_prod("comida","xbacon", 2, 6.50)
# # register_prod("comida","xtudo", 9, 7.50) #Aqui não deixa registrar pois tem mais que o limite por porção
# # register_prod("comida","xbauru", 2, 5.50)
# # register_prod("comida","xegg", 1, 6.50)
# # register_prod("comida","xalemao", 2, 7.50)
# # register_prod("comida","xporco", 2, 7.50) #Aqui não deixa entrar pois passa das 5 comidas permitidas no estoque. Essa seria a 6* comida
# # register_prod("bebida","coca", 1, 3.50)
# # register_prod("bebida","suco", 5, 6.00)
# # register_prod("bebida","agua coco", 2, 7.50)
# # register_prod("bebida","agua mineral", 2, 2.50) #Aqui não deixa entrar pois passa das 3 bebidas permitidas

# #Consultas
# # consulta_tabela("comida")
# # consulta_tabela("bebida")
# # print(consulta_preco("bebida","coca"))
# # print(consulta_qtde("comida","xsalada"))

# #Alterar quantidade ou preço
# alterar_qtde("comida","xsalada",2)
# alterar_qtde("comida","xegg",2)
# alterar_qtde("comida","xbauru",2)
# # alterar_preco("comida","xsalada",15.0)

# #Fazer pedidos
# fazer_pedido("comida","xnada", "xegg", "xbauru")
# # consulta_tabela("comida")
# # print(consulta_produtos("comida"))


############################################################################################################
###################################### SOLUCAO DO PROFESSOR ###############################################
############################################################################################################
# import sqlite3
# from random import choice

# conexao = sqlite3.connect("estoque.db")
# cursor = conexao.cursor()

# tabela_comida = """
# CREATE TABLE comidas (
# id integer primary key autoincrement,
# nome,
# preco,
# quantidade
# )
# """

# tabela_bebida = """
# CREATE TABLE bebidas (
# id integer primary key autoincrement,
# nome,
# preco,
# quantidade
# )
# """

# comidas = [("Hamburguer", 25.00, 5), ("Hotdog", 12.00, 5), ("Misto quente", 7.50, 5), ("Chocolate", 5.00, 5), ("Pão", 1.50, 5)]
# bebidas = [("Coca cola", 10.00, 7), ("Fanta", 8.00, 7), ("Café", 2.50, 5)]

# try:
#     cursor.execute(tabela_comida)
#     cursor.execute(tabela_bebida)

#     for comida in comidas:
#         registra_estoque_comida = f"""
#     INSERT INTO comidas (nome, preco, quantidade) 
#     VALUES ("{comida[0]}", {comida[1]}, {comida[2]})"""    
        
#         cursor.execute(registra_estoque_comida)

#     for bebida in bebidas:
#         registra_estoque_bebida = f"""
#     INSERT INTO bebidas (nome, preco, quantidade) 
#     VALUES ("{bebida[0]}", {bebida[1]}, {bebida[2]})"""    
        
#         cursor.execute(registra_estoque_bebida)

#     conexao.commit()

# except sqlite3.OperationalError:
#     pass

# def checa_quantidade(tabela, pedido):
#     if tabela == "comidas":
#         checa_estoque = f'''SELECT quantidade FROM comidas WHERE nome = "{pedido}"'''
#         cursor.execute(checa_estoque)
#         conteudo = cursor.fetchall()

#         if conteudo[0][0] == 0:
#             return False
#         else:
#             return conteudo[0][0]
    
#     elif tabela == "bebidas":
#         checa_estoque = f'SELECT quantidade FROM bebidas WHERE nome = "{pedido}"'
#         cursor.execute(checa_estoque)
#         conteudo = cursor.fetchall()

#         if conteudo[0][0] == 0:
#             return False
#         else:
#             return conteudo[0][0]

# def checa_preco(tabela, pedido):
#     if tabela == "comidas":
#         checa_estoque = f'''SELECT preco FROM comidas WHERE nome = "{pedido}"'''
#         cursor.execute(checa_estoque)
#         conteudo = cursor.fetchall()
#         return conteudo[0][0]
    
#     elif tabela == "bebidas":
#         checa_estoque = f'SELECT preco FROM bebidas WHERE nome = "{pedido}"'
#         cursor.execute(checa_estoque)
#         conteudo = cursor.fetchall()
#         return conteudo[0][0]    

# def cliente():
#     pedido = {}
#     pedido["comida"] = choice(comidas)[0]
#     pedido["bebida"] = choice(bebidas)[0]

#     if checa_quantidade("comidas", pedido["comida"]) == False:
#         print(f'O item {pedido["comida"]} está fora de estoque.')

#     elif checa_quantidade("bebidas", pedido["bebida"]) == False:
#         print(f'O item {pedido["bebida"]} está fora de estoque.')

#     else:
#         quantidade_atual_comida = int(checa_quantidade("comidas", pedido["comida"]))
#         quantidade_atual_bebida = int(checa_quantidade("bebidas", pedido["bebida"]))

#         atualiza_quantidade_comida = f'UPDATE comidas SET quantidade = {quantidade_atual_comida - 1} WHERE nome = "{pedido["comida"]}"'
#         atualiza_quantidade_bebida = f'UPDATE bebidas SET quantidade = {quantidade_atual_bebida - 1} WHERE nome = "{pedido["bebida"]}"'

#         cursor.execute(atualiza_quantidade_comida)
#         cursor.execute(atualiza_quantidade_bebida)
#         conexao.commit()

#         preco_comida = checa_preco("comidas", pedido["comida"])
#         preco_bebida = checa_preco("bebidas", pedido["bebida"])
#         preco_total = float(preco_comida) + float(preco_bebida)

#         print(f'Pedido feito! {pedido["comida"]} + {pedido["bebida"]}! Preço: R${preco_total:.2f}')

# for x in range(0, 30):
#     cliente()


###############################################################################################################
###############################################################################################################
###############################################################################################################
# ====================================================================================
# 1) Escreva um programa utilizando funções que realize um cadastro.
# Deverão ser coletadas as seguintes informações:

# CPF
# Nome
# Idade
# Sexo
# Cidade

# Os registros deverão ser armazenados em um arquivo CSV.
# Para manter o padrão brasileiro, o CSV será separado pelo caractere ";".
# O programa deverá possuir uma função de consulta e de exclusão (POR NOME OU CPF).
# O programa deverá possuir tratamentos de erro, com a finalidade de que o programa nunca
# dê uma exceção e também que ele não aceite dados incorretos em nenhum momento.

import csv
filename = "arquivo.csv"
aux=True

def define_file():
    try:
        with open(filename,"w") as file:
            cabecalho = ("CPF;NOME;IDADE;SEXO;CIDADE")
            file.write(cabecalho)
    except Exception:
        pass
    
def cadastrar(cpf,nome,idade,sexo,cidade):
    # try:
    l = [cpf,nome,idade,sexo,cidade]
    aux = validar(l)
    if aux == True:
        with open(filename,"a", newline='') as file:
            cadastro = (f"\n{cpf};{nome};{idade};{sexo};{cidade}")
            file.write(cadastro)
            print(f"{l[1]} cadastrado com sucesso")
    else:
        print("Dados Invalidos")
    # except Exception:
        # pass

def consultar(chave,valor):
    try:
        reg = False
        with open(filename, 'r',newline='') as file:
            csv_reader = csv.reader(file, delimiter=";")
            if chave.lower() == "nome":
                index = 1
            elif chave.lower() == "cpf":
                index = 0
            else:
                return("Coluna inválida")
        
            for row in csv_reader:
                if row[index] == valor:
                    reg = True
                    return f"Registro Encontrado: \n {row}"
            if reg == False:
                return(f"Registro ({valor}) não encontrado no arquivo")
    except Exception:
        pass

def deletar(chave,valor):
    remove = False
    conteudo = []
    new_conteudo = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=";")
        conteudo = list(csv_reader) #Cria uma lista com o conteúdo do arquivo

        if chave.lower() not in ["nome", "cpf"]:
            return f'Coluna inválida. Coluna "{chave}" não é uma chave válida nessa base de dados'
        
        if chave.lower() == "nome":
            col_index = 1
        else:
            col_index = 0

        new_conteudo.append(conteudo[0])

        for i in conteudo[1:]:
            if len(i) > col_index:
                if i[col_index] == valor:
                    remove = True
                else:
                    new_conteudo.append(i)
        if not remove:
            return f"Conjunto {chave} = {valor}, não existe no arquivo"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(new_conteudo)

def validar(info):
    for item in info:
        if info.index(item) == 0: #CPF
            if len(item) != 11:
                return False
            elif item.isdigit() == False:
                return False
        if info.index(item) == 1: #NOME
            pass 
        if info.index(item) == 2: #IDADE
            pass

        if info.index(item) == 3: #SEXO
            if item.isdigit() == True:
                return False

        if info.index(item) == 4: #CIDADE
            pass
    return True

# define_file()
# print(cadastrar("11111111111","Marcelo Lopes",37,"M","Hortolândia"))
# print(cadastrar("22222222222","Maria Lopes",27,"F","Campinas"))
# print(cadastrar("33333333333","Marcos Lopes",25,"M","Hortolândia"))
# print(cadastrar("44444444444","Marcosa Lopes",25,"M","Hortolândia"))
# print(cadastrar("55555555555","Marcose Lopes",25,"M","Hortolândia"))
# print(cadastrar("66666666666","Marcolino Lopes",25,"M","Hortolândia"))
# print(cadastrar("77777777777","Marilene Lopes",25,"M","Hortolândia"))
# print(cadastrar("77777777777","Noah Moraes","4","M","Oslo"))
# print(cadastrar("777777777778","Noah Lopes","4","M","Oslo"))
# print(consultar("cpf","44444444444"))
print(deletar("nome","Marcos Lopes"))
print(deletar("nome","Marcolino Lopes"))
print(deletar("cpf","77777777777"))



########################################################################################################################
# ====================================================================================
# 1) Escreva um programa utilizando funções que realize um cadastro.
# Deverão ser coletadas as seguintes informações:

# CPF
# Nome
# Idade
# Sexo
# Cidade

# Os registros deverão ser armazenados em um arquivo CSV.
# Para manter o padrão brasileiro, o CSV será separado pelo caractere ";".
# O programa deverá possuir uma função de consulta e de exclusão (POR NOME OU CPF).
# O programa deverá possuir tratamentos de erro, com a finalidade de que o programa nunca
# dê uma exceção e também que ele não aceite dados incorretos em nenhum momento.

# 1: Importar os modulos a serem usados.
# 2: Criamos uma função para o menu principal do programa.
# 3: Criar uma função para coletar as informações do cliente.
# 4: Criar uma função para validar as informações passadas pelo cliente.
# 5: Criar uma função para adicionar essas informações em um arquivo CSV.
# 6: Criar uma função para consultar o arquivo CSV.
# 7: Criar uma função para remover entradas do arquivo CSV.

# import csv, os

# def menu():
#     while True:
#         opcao = input("""O que deseja fazer? 
#                       1 - Consultar um valor no banco.
#                       2 - Cadastrar um valor no banco.
#                       3 - Remover um valor do banco.
#                       4 - Parar o programa.\n\n""")
        
#         os.system("cls" if os.name == "nt" else "clear")

#         if opcao == "4":
#             print("Parando o programa...")
#             break

#         elif opcao == "3":
#             exclusao()

#         elif opcao == "2":
#             cadastro()

#         elif opcao == "1":
#             consulta()

#         else:
#             print("Voce inseriu um valor inválido.\n")

# def cadastro():

#     while True:
#         cpf = input("Qual o CPF dessa pessoa? ")
#         if validacao("cpf", cpf) == False:
#             continue

#         nome = input("Qual é o nome da pessoa? ")

#         idade = input("Qual a idade da pessoa? ")
#         if validacao("idade", idade) == False:
#             continue

#         sexo = input("Qual o sexo da pessoa? [M/F/O]: ")
#         if validacao("sexo", sexo) == False:
#             continue

#         cidade = input("Qual a cidade onde essa pessoa reside? ")

#         dados_a_cadastrar = [cpf, nome, idade, sexo, cidade]
        
#         with open("banco.csv", "a", newline="") as arquivo:
#             conteudo = csv.writer(arquivo, delimiter=";")
#             conteudo.writerow(dados_a_cadastrar)

#         resposta = input("\nDeseja adicionar outro valor? [S/N]: ")
#         if resposta.upper() == "N":
#             break

#         os.system("cls" if os.name == "nt" else "clear")

# def validacao(teste, valor):
#     match teste:

#         case "cpf":
#             cpf = valor.replace(".", "").replace("-", "").strip()
#             if len(cpf) == 11 and cpf.isnumeric() == True:
#                 return True
#             else:
#                 print("CPF inválido, digite novamente.")
#                 return False

#         case "sexo":
#             sexo = valor.upper().strip()
#             if sexo in "MFO":
#                 return True
#             else:
#                 print("Sexo inválido, digite novamente.")
#                 return False

#         case "idade":
#             idade = valor.strip()
#             if idade.isnumeric() == True:
#                 if int(idade) < 130:
#                     return True
#             else:
#                 print("Idade inválida, digite novamente.")
#                 return False

#         case _:
#             pass

# def consulta():
#     while True:
#         resposta = input("""Por qual valor deseja consultar?
#                          0 - CPF
#                          1 - Nome\n\n""")
#         if resposta in "01":
#             resposta = int(resposta)
#             break
#         print("Opção inválida")

#     while True:
#         cpf_nome = input("Digite o nome ou cpf a consultar: ")
#         if resposta == 0:
#             if validacao("cpf", cpf_nome) == False:
#                 continue
#         break

#     with open("banco.csv", "r") as arquivo:
#         conteudo = csv.reader(arquivo, delimiter=";")
#         valor_encontrado = False

#         for linha in conteudo:
#             if linha[resposta] == cpf_nome:
#                 print(f"""Cadastro encontrado:
# CPF: {linha[0]}
# NOME: {linha[1]}
# IDADE: {linha[2]}
# SEXO: {linha[3]}
# CIDADE: {linha[4]}
# """)
#                 valor_encontrado = True
#                 break

#         if valor_encontrado == False:
#             print("Valor não encontrado")

# def exclusao():
#     cpf_nome = input("Digite o nome ou cpf da pessoa a excluir: ")

#     with open("banco.csv", "r") as arquivo_inicial, open("banco_editado.csv", "a", newline="") as arquivo_editado:
#         writer = csv.writer(arquivo_editado, delimiter=";")
#         reader = csv.reader(arquivo_inicial, delimiter=";")

#         for linha in reader:
#             if linha[0] != cpf_nome and linha[1] != cpf_nome:
#                 writer.writerow(linha)
        
#     os.remove("banco.csv")
#     os.rename("banco_editado.csv", "banco.csv")

# if __name__ == "__main__":
#     menu()
