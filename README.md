# Devil-s-Notebook

Este é o exemplo de código em python para exibir uma mensagem na tela:

print("Olá Mundo")

No sistema operacional Windows o interpretador Python deverá ser instalado para que possa ser utilizado, nos sistemas operacionais derivados de Linux na sua maioria já vem com o interpretador Python instalado por padrão, no macOS também. Para saber se o interpretador Python está instalado e qual sua versão utilize o comando a seguir:

python --version 

Caso não tenha o interpretador Python instalado, faça a instalação, é um pré-requisito para poder construir programas e scripts em Python.

Para entrar no prompt de comando do windows devo digitar cmd na barra de pesquisa do windows:

cmd

Para entrar no prompt do python digitar python:

python

Para sair do prompt do python digitar:

exit()

Identação no python(TAB) significa um bloco de código, em outras linguagens de programação usa-se {} em python usa-se a identação(TAB)

2 - Exercicios de programação

1 - Faça um programa que receba a como entrada dois números inteiros e faça a multiplicação entre esses dois números 

print("Bem vindo ao multiplicador")
num1=int(input("digite um numero inteiro: "))
num2=int(input("digite outro numero inteiro: "))
result=num1*num2
print("O resultado da multiplicação é : " ,result)

https://github.com/enthony17/Devil-s-Notebook/blob/main/multiplicador.py

2.2 - Faça um programa que pergunte ao usuario sua idade, o programa responde se ele é de maior ou menor de idade


idade=int(input("Qual sua idade: "))

if(idade>=18):
    print("Maior de idade. ")


else:
    print("Menor de idade")
    
https://github.com/enthony17/Devil-s-Notebook/blob/main/consultordeidade.py


3 - Game RENPY
Questões:

3.1 - O que é RENPY?

R: Renpy é uma Engine(biblioteca) para criação de games do tipo visual novel, utiliza a linguagem python

3.2 - Como Fazemos para instalar e criar um novo jogo no RENPY?

R: Acessamos o site oficial do renpy -> https://www.renpy.org/, realizamos o download, em seguida, descompactamos a pasta zip do jogo, e instalamos, , descompactada e mandamos a pasta game para um pasta vazia em seguida, entramos na pasta e executamos renpy.exe e passamos pelas configurações iniciais, clicamos em criar novo projeto e seguimos os passos que é pedido um dos passos é selecionar uma pasta ( no caso a que criamos e jogamos a pasta game dentro), abrimos a pasta criada no VS Code, ou outro editor de código, lá é possível fazer as mudanças e os acréscimos no game.

3.3 - Qual o comando para criar um novo personagem?

R:

 define f = Character('Fulano')

 define c = Character('Ciclano')
3.4 - Como exibir a fala do personagem?

R: É preciso anunciar qual personagem vai falar usando a letra definida

 label start:

     f "olá eu sou o Fulano. Qual seu nome?"

     c "Meu nome é Ciclano, prazer em conhece-lo Fulano"

     "Eu sou o narrador, a fala é dita diretamente sem especificar o personagem"
4 - Menu interativo RENPY
4.1 - Descreva como Criar um menu interativo na Engine RENPY, mostre um exemplo de código:

R: A menu declaração permite apresentar uma escolha ao jogador:

s "Sure, but what's a "visual novel?""

menu:

`"It's a videogame.":`
    `jump game`

`"It's an interactive book.":`
    `jump book`
label game:

`m "It's a kind of videogame you can play on your computer or a console."`

`jump marry`
label book:

`m "It's like an interactive book that you can read on a computer or a console."`

`jump marry`
label marry:

`"And so, we become a visual novel creating` duo."

## 5 - Exercícios Python
## 5.1 - Faça um programa que pergunte o nome do usuário e responda o usuário com: Seja bem vindo[nome do usuário].

## 5.2 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

C = 5 * ((F-32) / 9).

## 5.3 - Faça um programa que peça para o usuario digitar uma letra e verifique se a letra é vogal ou consoante
