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
