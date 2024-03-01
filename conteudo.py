#Python Collections
#Tuplas, Listas, Dicionarios, Sets

#--------------------------
#Tuplas: São imultáveis
#--------------------------

var1 = ("Arroz", "Queijo", "Leite", "Beterraba",40,False,("Feijao", "cenoura",3))
for item in var1:
    print(item)
print("item num 5=",var1[5])
print(type(var1))
print("Tamanho Var1 = ",len(var1))

#--------------------------
#Listas
#--------------------------
var2 = ["Arroz", "Queijo", "Leite", "Beterraba",40,False,("Feijao", "cenoura",3),40]
for item2 in var2:
    print(item2)
print("item num 5=",var2[5])
print(type(var2[4]))
print(var2.index(40))
print("Tamamnho Var2 = ",len(var2)) # Tamamnho Lista

#Remover items por nome
var2.remove("Beterraba")

#Remover items por index
var2.pop(2)

#Adicionar item no fim
var2.append("Salsicha")

#Adicionar item num index especifico
var2.insert(0,"Faca") #Added on index 0

print(var2)

for item in enumerate(var2):  # Enumera os items de list, tuplas ou até mesmo strings
    print(item)

#-----------------------------
#Dicionários
#-----------------------------
var3 = {"nome":"Marcelo", "idade":37,"cor":"azul"}

print(var3["nome"]) #Como referenciar Dicionario
var3["sobrenome"]="Moraes" #Como adicionar ao dicionário
var3["sobrenome"]="Costa" #Aqui "Costa" vai sobrescrever "Moraes"
print(var3)

#Maneiras de deletar
var3.pop("idade")
del(var3["cor"])

print(var3)

#-----------------------------
#Sets
#-----------------------------
#Compostos apenas por chaves
#Não aceita chaves repetidas

var4 = {"idade", "cachorro", 12,12,24,24,"cachorro"}
print(var4) #Mesmo tendo chaves repetidas ele retorna apenas os items sem os duplicados. Pode ser isado para converter

vard = ["idade", "cachorro", 12,12,24,24,"cachorro"] #criado uma lista
vard = set(var4) #converto a lista para set para remover duplicidades
print(vard)

#-----------------------------
#Funções
#-----------------------------

def soma(x, y):
    resultado = x + y
    print(resultado)


resp = int(input("Digite um numero: "))

soma(resp, 25)

soma(77, 25)

def soma(x, y):
    resultado = x + y
    return resultado
    

resp = int(input("Digite um numero: "))
resp2 = int(input("Digite outro numero: "))
print(f"A soma de {resp} e {resp2} é {soma(resp, resp2)}")

var1 = soma(20,30) #var1 vai ter o resultado da função

def soma(*,x,y): #esse * indica que eu preciso chamar a função apontado quem é X e quem é Y. Ex: soma(x=20,y=10)
    resultado = x+y
    return resultado

def soma(x,y,/): #essa / indica que eu preciso chamar a função apontado somente números, não vai aceitar passar declarando x e y como acima
    resultado = x+y
    return resultado

def soma(x=10,y): #O X nesse caso é opcional, ele vai receber o valor 10 caso não seja passado, se for passado, ele recebe o valor passado
    resultado = x+y
    return resultado

#Quando não sei o número de argumentos a serem passados pode-se usar o * assim:
def mult(*x) #os números passados farão partes de uma tupla
    return(x)
print(mult(10,20,30,40))

#Também é possível algo do tipo:
def mult(*x, y)
    return(x)
print(mult(10,20,30,40))

#Use Case interessante
def mult(*x,y=5): #Tupla X e Y
    for valor in x:
        print(f"{valor} x {y} = {valor * y}")
mult(10,32,2,12, y=10) #O y= é necessário aqui para o Python identificar onde começa o próximo operando, sem o y= ele identificaria o prox operando com send x ainda.
#Cada X é multiplicado pelo Y

#Caso eu passe mais argumentos, ou número indeterminado de argumentos para a função use **
def diff(a,**chaves): # Os argumentos são transformados em um dictionary - chave+valor
    for valor in chaves.values():
        print(f"{a} - {valor} = {a-valor}")


diff(a=10,b=20,c=30) #Na função diff isso será transformado 
diff(a=13,b=24,c=36,d=56)

########################
#Funções
########################
#na definição de uma função podemos defini-la com quantidade variável de argumentos
#Exemplo
def diff(a,**chaves) #Esse **chaves diz que a variável chaves é um dicionário e pode ser passado um número indeterminado de argumentos
def diff(a,*chaves) #Esse *chaves diz que a variável chaves é uma lista e pode ser passado um número indeterminado de argumentos

#-----------------------------
#Funções Lambda
#-----------------------------
#Funções Lambda / Funções anônimas
        
    
def soma1(x, y):
    return(x + y)

soma2 = lambda x, y: x + y #Definição da Função é feita de forma simplista assim. Essa é só a definição

print(soma1(10, 15))
print(soma2(10, 15)) #Para chamar, note que até a cor é diferente, pois soma2 é uma variável que tem o resultado da função Lambda

#-----------------------------
#Módulos
#-----------------------------
#Existem módulos nativos (print, input)
#Existem módulos NATIVOS, já no pacote do Python, mas não carregados por padrão (os, math, random, etc)
#Existem módulos não NATIVOS que não estão no pacote Python e podem ser baixados pelo gerenciador de pacotes PIP (flask, pymongo)
# 
#Os imports podem ser feitos para módulos que foram baixados
#Digamos que baixamos um módulo chamado "modulo baixado"


#"Digamos que tem várias funções dentro desse módulo, e uma delas chamada "imprime_mensagem""
#Para utilizar essa função desse módulo
import modulo_baixado
modulo_baixado.imprime_mensagem()


#É também possível IMPORTAR apenas a função desejada dentro do "modulo_baixado"
from modulo_baixado import imprime_mensagem()

#Tambem podemos importar um dicionário ou qualquer objeto de um outro arquivo.
#Exemplo de um arquivo no nosso diretório chamado "modulo_baixado"
import modulo_baixado
modulo_baixado.imprime_mensagem()

#-----------------------------
#Arquivos
#-----------------------------
#modos de open - 
#w - write overwriting
#r - read
#a - append. Does not overwrite, just append the content
#There are several other options available but these are the most commons

arquivo = open("path/do/arquivo", "")

conteudo = "Primeira linha do meu arquivo"
arquivo.write(conteudo)

arquivo.close() #Não esquecer de fazer o close

arquivo = open("teste.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


#Outra maneira de fazer o open
with open("test.txt","a" ) as arquivo:
    conteudo = "teste"
    arquivo.write(conteudo) 

#-----------------------------
#Arquivos CSV
#-----------------------------
import csv
    
    with open("arquivo.csv","a") as planilha:
        conteudo = csv.reader(planilha, delimiter=";")
        print(conteudo) #Só vai mostrar a posição da memoria contendo o csv. Devemos pedir qual registro vc quer do csv para ter algo printavel
        print(next(conteudo)) #Aqui sim mostra qual o prox registro
        for linha in conteudo: #Outra maneira
            print(linha)

#############################################################
arquivo = open("teste.txt", "a")
conteudo = "Primeira linha do meu arquivo\n"
arquivo.write(conteudo)
arquivo.close()

arquivo = open("teste.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

with open("teste.txt", "a") as arquivo:
    conteudo = "Linha adicionada com o WITH\n"
    arquivo.write(conteudo)

# ================================================
#csv
    
with open("arquivo.csv", "r") as planilha:
    conteudo = csv.reader(planilha, delimiter=";")
    # Generator
    print(next(conteudo))
    for linha in conteudo:
        print(linha)



#-----------------------------
#Programação Orientada a Objetos            
#Classes - (Tipos de Objetos)
#----------------------------
#Criação de uma classe (tipo de objeto) para simular uma PILHA

#Classes no Pthon começa com letras maiúsculas
class Pilha: 
    def __init__(self): # __init__(self) é a função que inicia uma classe
        self.pilha = [] #Todo objeto que for uma Pilha, um tipo de objeto Pilha, todas elas terão essa variável "pilha" que será uma lista[]
        self.limite = 10
        self.qtd = 0


    def empilhar(self, item): # Toda vez que formos usar na função algum objeto de dentro da classe, o self precisa ser passado
        if self.qtd <= 10:
            self.pilha.append(item)
            self.qtd += 1
            return(f"{item} adicionado à pilha")
        else:
            return(f"Essa pilha já tem 10 itens nela")

    def desempilhar():
        if self.qtd > 0:
            del self.pilha[-1] #Poderia ser usado self.pilha.pop(-1). Esse "del" pode deletar quase qulquer objeto no Python, só uma outra opção
            self.qtd -= 1
            return(f"item removido")
        else:
            return(f"A pilha está vazia")


pilha_de_pratos = Pilha() # A letra maiúscula identifica uma classe, não uma função
pilha_de_brinquedos = Pilha()

pilha_de_pratos.empilhar("prato azul")
pilha_de_pratos.empilhar("prato branco")
pilha_de_pratos.empilhar("prato preto")



print(pilha_de_pratos.empilhar("prato azul"))
print(pilha_de_pratos.empilhar("prato branco"))
print(pilha_de_pratos.empilhar("prato preto"))
print(pilha_de_pratos.desempilhar("prato azul"))

#-----------------------------
#Encapsulamento
# Traz um certo isolamento e proteção às variáveis da classe pois o normal de se ter acesso de fora da classe seria o acesso às funções apenas
# Para promover o encapsulamento adiciona duplo underline na frente da variável "__var" por exemplo
# Não consigo dar um printi por exemplo nas variáveis adicionada com __ dentro da clases
#----------------------------

class Pilha: 
    def __init__(self): # __init__(self) é a função que inicia uma classe
        self.__pilha = [] #Todo objeto que for uma Pilha, um tipo de objeto Pilha, todas elas terão essa variável "pilha" que será uma lista[]
        self.__limite = 10
        self.__qtd = 0


    def empilhar(self, item): # Toda vez que formos usar na função algum objeto de dentro da classe, o self precisa ser passado
        if self.__qtd <= 10:
            self.__pilha.append(item)
            self.__qtd += 1
            return(f"{item} adicionado à pilha")
        else:
            return(f"Essa pilha já tem 10 itens nela")

    def desempilhar():
        if self.__qtd > 0:
            del self.__pilha[-1] #Poderia ser usado self.pilha.pop(-1). Esse "del" pode deletar quase qulquer objeto no Python, só uma outra opção
            self.__qtd -= 1
            return(f"item removido")
        else:
            return(f"A pilha está vazia")


pilha_de_pratos = Pilha() # A letra maiúscula identifica uma classe, não uma função
pilha_de_brinquedos = Pilha()

pilha_de_pratos.empilhar("prato azul")
pilha_de_pratos.empilhar("prato branco")
pilha_de_pratos.empilhar("prato preto")



print(pilha_de_pratos.empilhar("prato azul"))
print(pilha_de_pratos.empilhar("prato branco"))
print(pilha_de_pratos.empilhar("prato preto"))
print(pilha_de_pratos.desempilhar("prato azul"))


#-----------------------------
#Herança
# Classes que são subclasses de outras
# Suporndo que temo uma empresa e temos os funcionários dessa empresa
# Classe "Funcionário"
#---Classe |_"Gerente" 
#----------------------------

class Funcionario:

    def __init__(self):
        self.nome = ""
        self.salario = "" 
        self.idade = ""

    def checa_nome(self):
        return(self.nome)
    
    def set_salario(self,salario):
        self.salario=salario
    
class Gerente(Funcionario): # É uma subclasse de classe Funcinário

    def __init__(self):
        super().__init__()  # Palavra chave "super" precisa ser passado para herdar as características da classe Funcionário
        self.bonus = 1.5
    
    def aplica_bonus(self):
        self.salario = self.salario * self.bonus

joao = Funcionario()
joao.set_salario(2000)
pedro = Gerente()
pedro.set_salario(3000)
pedro.aplica_bonus()

#-----------------------------
#Polimorfismo
# Você consegue alterar o valor dos atributos da classe
#----------------------------


class Funcionario:

    def __init__(self):
        self.salario = 2000
        self.idade = 30

    def set_salario(self,salario):
        self.salario=salario
    
class Gerente(Funcionario): # É uma subclasse de classe Funcinário

    def __init__(self):
        super().__init__()  # Palavra chave "super" precisa ser passado para herdar as características da classe Funcionário
        self.salario = 3000
        # self.salario = self.salario * 1.5 --- Só uma outra forma de fazer um polimorfismo com uma conta
    
    def aplica_bonus(self):
        self.salario = self.salario * self.bonus


#-----------------------------
#Tratamento de Exceções / Erros
#----------------------------
 #Existem tipos de Exceções nativas do Python: Exemplo -> ValueError
#Lista de Exceções
        
# BaseException
# +---Exception
# | +---TypeError
# | +---StopAsyncIteration
# | +---StopIteration
# | +---ImportError
# | | +---ModuleNotFoundError
# | | +---ZipImportError
# | +---OSError
# | | +---ConnectionError
# | | | +---BrokenPipeError
# | | | +---ConnectionAbortedError
# | | | +---ConnectionRefusedError
# | | | +---ConnectionResetError
# | | +---BlockingIOError
# | | +---ChildProcessError
# | | +---FileExistsError
# | | +---FileNotFoundError
# | | +---IsADirectoryError
# | | +---NotADirectoryError
# | | +---InterruptedError
# | | +---PermissionError
# | | +---ProcessLookupError
# | | +---TimeoutError
# | | +---UnsupportedOperation
# | | +---ItimerError
# | +---EOFError
# | +---RuntimeError
# | | +---RecursionError
# | | +---NotImplementedError
# | | +---_DeadlockError
# | +---NameError
# | | +---UnboundLocalError
# | +---AttributeError
# | +---SyntaxError
# | | +---IndentationError
# | | | +---TabError
# | +---LookupError
# | | +---IndexError
# | | +---KeyError
# | | +---CodecRegistryError
# | +---ValueError
# | | +---UnicodeError
# | | | +---UnicodeEncodeError
# | | | +---UnicodeDecodeError
# | | | +---UnicodeTranslateError
# | | +---UnsupportedOperation
# | +---AssertionError
# | +---ArithmeticError
# | | +---FloatingPointError
# | | +---OverflowError
# | | +---ZeroDivisionError
# | +---SystemError
# | | +---CodecRegistryError
# | +---ReferenceError
# | +---BufferError
# | +---MemoryError
# | +---Warning
# | | +---UserWarning
# | | +---DeprecationWarning
# | | +---PendingDeprecationWarning
# | | +---SyntaxWarning
# | | +---RuntimeWarning
# | | +---FutureWarning

#Podemos tratar cada tipo se exception dessas

#Tratamento de Exceções:

try:
    print(int("cinquenta")) #Tentando converter a string cinquenta em int 50

except ValueError:
    print("O programa deu uma exceção de ValueError")

except TypeError:
    print("Você teve um TypeError")

except Exception:
    print("Houve uma exceção")

else: #Em caso de não erro, executa o ELSE. --- OPCIONAL
    print("Trecho executado se o TRY for bem sucedido")

finally: # É executado toda vez, independente do que acontecer pra cima. --- OPCIONAL
    print("Esse trecho sempre executado no fim")

#A Maioria dos módulos que são importados já têm suas exceções configuradas
    

#-----------------------------
#BANCO DE DADOS
#----------------------------

#SQL --> Armazena informações em forma de tabela tipo linhas e colunas
import sqlite3

#Criação de Banco de Dados
conexao_com_banco = sqlite3.connect("path/para/db/nome.db") #Cria ou conecta-se com um banco de dados existente
cursor = conexao_com_banco.cursor()                         #Cursor é criado para editar o banco

#criação de tabela
cria_tabela = """ 
CREATE TABLE funcionarios (
id integer primary key autoincrement,
nome text,
idade integer
)
"""

#Adicionar ITENS
adiciona_valores =""" 
INSERT INTO funcionarios(nome, idade)
VALUES ("Marcelo", 37)
"""

#Remover ITENS
remove_valores ='DELETE FROM funcionarios WHERE nome = "Marcelo"'

#Atualizar / Update Table
update_valores ='UPDATE funcionarios SET idade = 35 WHERE nome = "Marcelo"'

#Select, Ler Tabela
select_valores = 'SELECT idade FROM funcionarios WHERE nome = "Marcelo"'
select_valores = 'SELECT * FROM funcionarios WHERE nome = "Marcelo"'





cursor.execute(cria_tabela)
conexao_com_banco.commit() #Commit salva o que se faz na tabela, por isso não é necessário no SELECT


cursor.execute(adiciona_valores)
conexao_com_banco.commit() #Commit salva o que se faz na tabela, por isso não é necessário no SELECT


cursor.execute(remove_valores)
conexao_com_banco.commit() #Commit salva o que se faz na tabela, por isso não é necessário no SELECT

#Para imprimir 
conteudo = cursor.fetchall() # Variavel conteudo terá o conteudo do que o cursor executou
print(conteudo)

conexao_com_banco.close()



##################################################################################
# Bancos de dados do TIAGO PROFESSOR
# SQL -> Armazena informações em uma forma de Tabela.
######################################################################################
import sqlite3

conexao = sqlite3.connect("empresa.db")  # Cria ou se conecta a um banco de dados existente.
cursor = conexao.cursor()                # Utilizado pra editar o banco.

# Criamos o comando pra gerar uma tabela:
cria_tabela = """
CREATE TABLE funcionarios (
id integer primary key autoincrement, 
nome text, 
idade integer
)"""

# Executamos um comando, salvamos e fechamos a conexão:
cursor.execute(cria_tabela)
conexao.commit()

# Criamos o comando pra adicionar um item em uma tabela:
adiciona_funcionario1 = """
INSERT INTO funcionarios (nome, idade) 
VALUES ("Tiago", 27)"""

adiciona_funcionario2 = """
INSERT INTO funcionarios (nome, idade) 
VALUES ("Kaique", 30)"""

adiciona_funcionario3 = """
INSERT INTO funcionarios (nome, idade) 
VALUES ("Caio", 28)"""

cursor.execute(adiciona_funcionario1)
cursor.execute(adiciona_funcionario2)
cursor.execute(adiciona_funcionario3)
conexao.commit()

# Criamos o comando pra remover um item de uma tabela:
remove_funcionario = 'DELETE FROM funcionarios WHERE nome = "Tiago"'
cursor.execute(remove_funcionario)
conexao.commit()

# Criamos o comando pra editar um valor na tabela:
atualiza_valor = 'UPDATE funcionarios SET idade = 28 WHERE id = 2'
cursor.execute(atualiza_valor)
conexao.commit()

# Criamos o comando pra checar o conteudo da tabela:
checa_tabela = "SELECT * FROM funcionarios"
# checa_tabela = "SELECT idade FROM funcionarios"
# checa_tabela = "SELECT * FROM funcionarios WHERE nome = 'Tiago'"
cursor.execute(checa_tabela)
conteudo = cursor.fetchall()

for linha in conteudo:
    print(linha)

conexao.close()

######################################################################################################################
## GENERATORS - Você não tem acesso a todo conteudo de um generator, você precisa pedir item por item para acessá-los
######################################################################################################################

def cria_lista(x):
    lista = []
    for numero in range(0, x):
        lista.append(numero)
    return lista

def cria_generator(x):
    lista = []
    for numero in range(0, x):
        lista.append(numero)
        yield lista # yield é a keywork que gera um generator



print(cria_lista(26)) #--> Aqui ele traz o conteúdo da lista
print(cria_generator(26)) # --> Aqui por ser generator ele não da o display

print(next(cria_generator)) #Aqui ele traz o primeiro
print(next(cria_generator)) #Aqui ele traz o segundo, e não importa onde se é chamado. O ponteiro não zera, somente no fim do generator EOF
print(next(cria_generator)) #Aqui ele traz o segundo, e não importa onde se é chamado. O ponteiro não zera, somente no fim do generator EOF
 #Se for passar o generator dentro de um FOR, não precisa da keyword "next", no FOR ele funciona mesmo sem o "next"

##################################################################################
# GENERATOR COMPREHENSIONS
##################################################################################
#Outro jeito de syntaxe

#Para algo desse tipo
def gen()
    for x in range(0, 10):
        yield x
gencomp = gen()

#Podemos usar generator comprehensions
gen comp = (x for x in range(0,10)) #Por serem generators, fica entre parentesis


###############################################
#LIST COMPREHENSIONS
###############################################
#Outro jeito de syntaxe

#Para algo desse tipo
def cria_lista(x):
    lista = []
    for numero in range(0, x):
        lista.append(numero * 2)
    return lista
#Podemos usar LIST COMPREHENSION
lista_comp = [x * 2 for x in range(0, 15)] #Para cada valor de x numa range até 15, ele faz esse número * 2. Usa-se [] pois o resultado será uma lista
#A primeira informação (x * 2 por exemplo) diz como será gerado o resultado
print(lista_comp)

###############################################
#DICTIONARY COMPREHENSIONS
###############################################
#Outro jeito de syntaxe

#Para algo desse tipo
def gera_dict():
    dicionario = {}
    for num in enumerate(range(550, 560))  #Aqui o Enumerate cria uma tupla com duas posições, posição[0] é o número do Enumerate e posição[1] é o valor
        dicionario[num[0]] = num[1]
    return dicionario
#OU
def gera_dict():
    dicionario = {}
    for chave, valor in enumerate(range(550, 560))  #Aqui o Enumerate cria uma tupla com duas posições, posição[0] é o número do Enumerate e posição[1] é o valor
        dicionario[chave] = valor #Na variavel dicionario, atribua o valor de "valor" na chave
    return dicionario

#Podemos usar DICITIONARY COMPREHENSION
dict_comp = {chave : valor for chave, valor in enumerate(range(550, 560))}
print(dict_comp)

####################################################################
# map, reduce, filter
####################################################################
##############################
#map
#############################
quadrado = lambda x: x**2
lista = [1, 2, 3, 4, 5]

def quadrado2(x):
    return x**2

map (quadrado2, lista) #MAP aplica a função "quadrado" a todos os componentes de lista
map(quadrado, lista) #MAP aplica a função "quadrado" a todos os componentes de lista

######################################################
#reduce --> Tenta reduzir o num de objetos de uma coleção
# Ele pega dois parametros, realiza o codigo da função passada, e o resultado é usado com o próximo item no objeto passado como segundo parametro
######################################################
from functools import reduce
lista = [1, 2, 3, 4, 5]

def soma(x ,y):
    return x + y

soma2 = lambda x, y: x + y

print(reduce(soma, lista)) # Passado a lista, e a função, ele pega os dois parametros passados, realiza a função, e o resultado é usado na função novamente com o próximo objeto da coleção passada como segundo argumento, nesse caso uma lista
print(reduce(soma2, lista))

##################################################
#filter
#################################################
#filter
temperaturas = [25, 30, 35, 36, 12, 21, 41, 22, 36]

sub_30 = lambda x: x < 30
print(list(filter(sub_30, temperaturas)))

##################################################
# É comum ver algo do tipo:
##################################################
if __name__ == "__main__":
    menu()

# Isso é usado para o caso de se ter uma função solta ou algum código fora de função e ao se
#importar esse arquivo, eu não saia executando tudo, já que ao se importar um código, tem-se acesso
#a tudo que ele tem, o que não estiver isolado por função, acaba executando automaticamente se não 
#tratado por essa condição: if __name__ == "__main__":
#No caso acima, o menu() por exemplo só seria executado se executado do arquivo root de origem, 
#ele não executa se ele for importando em outro código, pois vai cair nessa condição, e saberá que 
#o arquivo chamando não é o __main__ que seria o arquivo de origem, conhecido pelo Python
