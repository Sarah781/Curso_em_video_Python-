#Condições simples e compostas

#Desafio 28 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
comp=randint(0,5) #faz o computador pensar
jogador=int(input('Estou pensando em um número de 0 a 5! Tente advinhar:')) #jogador tenta advinhar
if jogador == comp:
    print('Você acertou :)')
else:
    ('Não foi dessa vez')


#Desafio 29 Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mesnagem dizendo que ele foi multado 
#A multa vai custar R$7,00 por cada km acima do limite

velocidade=float(input('Velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado! Sua multa custará R${:.2f}!'.format((velocidade-80)*7))
else:
    print('Você está andando na linha!')


#Desafio 30 Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num=int(input('Insira um número inteiro: '))
resultado= num % 2
if resultado == 0:
    print('É um número {} é par'.format(num))
else:
    print('É um número {} é ímpar'.format(num))
 

#Desafio 31 Desenvolva um programa que pergunte a distância de um viagem em km. 
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas

d=float(input('Qual a distância da sua Viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(d))
if d <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(d*0.50))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(d*0.45))    

#Desafio 32 Faça um programa que leia o ano qualquer e mostre se ele é bissexto

from datetime import date
ano=int(input('Insira um ano ou coloque 0 para o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

#Desafio 33 Faça um programa que leia três números e mostre qual é o maior e qual o menor

n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
n3=int(input('Terceiro valor: '))

#verificando quem é o menor
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3

#verificando quem é o maior
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3

#print('O menor número é {}'.format(menor))
#print('O maior número é {}'.format(maior))

#Desafio 34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
#Para salários superiores a R$1250.00, calcule um aumento de 10%
#Para os inferiores ou iguais,o aumento é de 15%

salario=float(input('Qual é o salário do funcionário? R$'))
if salario <=1250:
    novo=salario+(salario*15/100)
else:
    novo=salario+(salario*10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario,novo))


#Desafio 35 Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo

a=float(input('Primeira reta: '))
b=float(input('Segunda reta: '))
c=float(input('Terceira reta: '))
if a<b+c and b<a+c and c<a+b:
    print('As retas acima PODEM formar triângulo')
else:
    print('As retas acima NÃO PODEM formar triângulo')