
# Dicionário que contém os anos de lançamento, quantidade de páginas e autores de 25 livros
livraria = {
    'Dom Casmurro': {'ano': 1899, 'paginas': 256, 'autor': 'Machado de Assis'},
    'Harry Potter E A Pedra Filosofal': {'ano': 1997, 'paginas': 223, 'autor': 'J.K. Rowling'},
    '1984': {'ano': 1949, 'paginas': 336, 'autor': 'George Orwell'},
  'Aristóteles e Dante descobrem os segredos do universo': {'ano': 2014, 'paginas': 390, 'autor': "Benjamin Alire Sáenz"},
  'Todo Esse Tempo': {'ano': 2020, 'paginas': 352, 'autor': 'Mikki Daughtry'},
  'Mentirosos': {'ano': 2014, 'paginas': 272, 'autor': 'E. Lockhart'},
  'Tartarugas Até Lá Embaixo': {'ano': 2017, 'paginas': 256, 'autor': 'John Green'},
  'A Revolução Dos Bichos': {'ano': 2007, 'paginas': 152, 'autor': 'George Orwell'},
  'O Colecionador': {'ano': 2018, 'paginas': 256, 'autor': 'John Fowles'},
  'O Diário De Anne Frank': {'ano': 2020, 'paginas': 224, 'autor': 'Anne Frank'},
  'Hamlet': {'ano': 1601, 'paginas': 112, 'autor': 'William Shakespeare'},
  'Extraordinário': {'ano': 2013, 'paginas': 320, 'autor': 'R.J. Palacio'},
  'O Pequeno Príncipe': {'ano': 2018, 'paginas': 96, 'autor': 'Antoine de Saint-Exupéry'},
  'O Alquimista': {'ano': 2017, 'paginas': 208, 'autor': 'Paulo Coelho'},
  'Hábitos Atômicos': {'ano': 2019, 'paginas': 320, 'autor': 'James Clear'},
  'Pequeno Manual Antirracista': {'ano': 2019, 'paginas': 136, 'autor': 'Djamila Ribeiro'},
  'Sobrevivendo No Inferno': {'ano': 2018, 'paginas': 160, 'autor': "Racionais MC's"},
  'A Parte Que Falta': {'ano': 2018, 'paginas': 112, 'autor': 'Shel Silverstein'},
  'Com amor, Simon': {'ano': 2018, 'paginas': 272, 'autor': 'Becky Albertall'},
  'Vermelho, Branco e Sangue Azul': {'ano': 2019, 'paginas': 392, 'autor': 'Casey McQuiston'},
  'Maus': {'ano': 2021, 'paginas': 296, 'autor': 'Vladeck Spiegelman'},
  'Dom Quixote': {'ano': 2018, 'paginas': 232, 'autor': 'Miguel Cervantes'},
  'Entendendo Algoritmos': {'ano': 2017, 'paginas': 264, 'autor': 'Aditya Y. Bhargava'},
  'O Codificador Limpo': {'ano': 2012, 'paginas': 244, 'autor': 'Robert C. Martin'},
  'Código Limpo': {'ano': 2009, 'paginas': 425, 'autor': 'Robert C. Martin'},
}

# Contador que servirá como controle da quantidade de livros selecionados pelo usuário
num_livros = 0

# Lista vazia criada com o intuito de guardar os livros escolhidos posteriormente
livros_selecionados = []

print("Seja bem-vindo(a) à nossa livraria pública!")
nome = input("Para começarmos seu atendimento, poderia nos dizer qual é o seu nome? ")
nome = nome.strip().capitalize()

print("{}, antes de nos dizer o que você está buscando, é preciso ressaltar que só é possível levar até 3 livros da nossa biblioteca.".format(nome))


escolha = int(input("Você deseja retirar quantos livros? "))

# Laço responsável por assegurar que serão escolhidos até 3 livros
while escolha > 3:
  print("Você só pode pegar até 3 livros. Tente novamente! ")
  escolha = int(input("Você deseja pegar quantos livros? "))
  if escolha <= 3:
    break

# Laço que repete a pergunta a partir do número que o usuário indicar
while num_livros < 3 and num_livros < escolha:
  livro = input("Digite o título do livro desejado: ")
  livro = livro.strip().title()

# Condição que percorre o dicionário criado à procura do título inserido e, em caso de correspondência, organiza as informações do livro e adiciona ele na lista criada por meio do .append
  if livro in livraria:
   livro_selecionado = {
    'nome': livro,
    'ano': livraria[livro]['ano'],
    'paginas': livraria[livro]['paginas'],
    'autor': livraria[livro]['autor']
    }
   livros_selecionados.append(livro_selecionado)
   num_livros += 1
  
  else:
   print("Desculpe, o livro que você está buscando não está disponível em nossa livraria.")

print("Ok! Agora preciso que você me informe seu número de telefone e endereço, para que eu possa fazer seu cadastro.")

telefone = int(input("Qual seu número de telefone? "))
endereco = input("Qual seu endereço? ")

import time

print("{}, aqui está sua ficha cadastral!".format(nome))

# São imprimidas na tela as informações que o usuário inseriu e os dados dos livros que estão presentes no dicionário 'livraria'
print("\n-----------------")
print("Nome: {}".format(nome))
print("Endereço: {}".format(endereco))
print("Telefone: {} ".format( telefone))
print("-----------------")

print("\n▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n")
print("       Livros retirados:     \n")

for livro in livros_selecionados:
  print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪▪︎▪︎")
  print("Nome:", livro['nome'])
  print("Autor(a):", livro['autor'])
  print("Ano de lançamento:", livro['ano'])
  print("Quantidade de páginas:", livro['paginas'])
  print("▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪▪︎\n")
  time.sleep(2)

print("\n Lembre-se: O prazo de devolução é de 20 dias. Obrigada e boa leitura!")