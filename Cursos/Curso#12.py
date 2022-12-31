#if 
#elif
#else


#nome=str(input('Qual o seu nome: '))
#if nome == 'Sarah':
#    print('Que nome lindo!')
#elif nome == 'Wesley':
#    print('Seu nome é maravilhoso!')
#else:
#    print('Seu nome é normal')
#print('Tenha um Bom dia, {}!'.format(nome))


#______________________________________________________________________________________________

#Desafio 36 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

a=float(input('Valor da casa: R$'))
b=float(input('Salário do comprador: R$'))
c=int(input('Em quantos anos ele vai pagar: '))
pm=a/(c*12)
min=b*30/100
if pm <= min:
    print('Empréstimo aceito')
else:
    print('Empréstimo negado')

#______________________________________________________________________________________________

#Desafio 37 Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a
#base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

num=int(input('Insira um numero: '))
print('Escolha a base de conversão:\n1 para binário \n2 para octal \n3 para hexadecimal')
opcao=int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num,bin(num)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num,oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num,hex(num)))
else:
    print('Opção inválida!')

 

#______________________________________________________________________________________________

#Desafio 38 Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior 
#Não existe valor maior, os dois são iguais 

v1=int(input('Insira um número: '))
v2=int(input('Insira mais um número: '))
if v1 > v2:
    print('O primeiro número é maior')
elif v2 > v1:
    print('O segundo número é maior')
else:
    print('Não existe número maior, os dois são iguais')

#______________________________________________________________________________________________

#Desafio 39 Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
#se ele ainda vai se alistar ao serviço militar.
#se é a hora de se alistar.
#se já passou do tempo do alistamento
#O programa deverá mostrar o tempo que falta ou que já passou do prazo


from datetime import date
ano=int(input('Qual o ano do seu nascimento: '))
idade=date.today().year - ano
if idade < 18:
    faltam=18-idade
    print('Faltam {} anos para o alistamento'.format(faltam))
elif idade == 18:
    print('Você tem que se alistar agora')
elif idade > 18:
    passou=idade-18
    print('Seu alistamento foi a {} anos atrás'.format(passou))

#print('Você tem {} anos'.format(idade))

#______________________________________________________________________________________________

#Desafio 40 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando um mensagem no final
#de acordo com a média atingida:
#Média abaixo de 5.0: Reprovado
#Média entre 5.0 e 6.9: Recuperação
#Média 7.0 ou acima: Aprovado

n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
media=(n1+n2)/2
if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media > 7.0:
    print('APROVADO')

#______________________________________________________________________________________________

#Desafio 41 A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:
#até 9 anos:mirim
#até 14 anos:infantil
#até 19 anos:júnior
#até 20 anos:sênior
#acima:master

from datetime import date
ano=int(input('Qual o ano do seu nascimento: '))
idade=date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade <=9:
    print('Classificação: Mirim')
elif idade >=10 and idade <=14:
    print('Classificação: Infantil')
elif idade >=15 and idade <=19:
    print('Classificação: Júnior')
elif idade ==20:
    print('Classificação: Sênior')
elif idade > 20:
    print('Classificação: Master')

#______________________________________________________________________________________________

#Desafio 42 refaça o desafio 35 dos triângulos acrescentandoo o recurso de mostrar que tipo de triângulo será formado
#equilátero: todos os lados iguais
#isósceles: dois lados iguais
#escaleno: todos os lados diferentes

a=float(input('Primeira reta: '))
b=float(input('Segunda reta: '))
c=float(input('Terceira reta: '))
equilátero= a==b==c
isósceles= a==b or a==c or b==c or b==a or c==a or c==b
escaleno= a != b != c != a
if equilátero:
    print('As retas acima PODEM formar triângulo Equilátero')
elif isósceles:
    print('As retas acima PODEM formar triângulo Isósceles')
elif escaleno:
    print('As retas acima PODEM formar triângulo Escaleno')
else:
    print('As retas acima NÃO PODEM formar triângulo')


#______________________________________________________________________________________________

#Desafio 43 desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status 
#de acordo com a tabela abaixo:
#abaixo de 18.5:abaixo do peso
#entre 18.5 e 25: peso ideal
#25 até 30:sobrepeso
#30 até 40:obesidade
#acima de 40: obesidade mórbida

peso=float(input('Qual o seu peso: Kg '))
altura=float(input('Qual sua altura: m '))
imc=peso/(altura**2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >=18.5 and imc <25.0:
    print('Peso ideal')
elif imc >=25.0 and imc <30.0:
    print('Sobrepeso')
elif imc >=30.0 and imc <40.0:
    print('Obesidade')
elif imc>40.0:
    print('Obesidade Mórbida')

#______________________________________________________________________________________________

#Desafio 44 elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e
#condição de pagamento
#a vista dinheiro/cheque:10% de desconto
#a vista no cartão:5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão:20% de juros 

preço=float(input('Preço das Compras: R$'))
print('Escolha sua opção:\n[1] a vista dinheiro/cheque \n[2] a vista no cartão \n[3] em até 2x no cartão \n[4] 3x ou mais no cartão')
opcao=int(input('Sua Opção: '))
if opcao == 1:
    print('Você recebeu 10%'' de desconto então o valor final é {:.2f}'.format(preço-(preço*10/100)))
elif opcao == 2:
    print('Você recebeu 5%''de desconto então o valor final é {:.2f}'.format(preço-(preço*5/100)))
elif opcao == 3:
    print('Você pagará 2x de {:.2f}'.format(preço/2))
elif opcao == 4:
    print('Você terá juros de 20%'' então o valor final é {:.2f}'.format(preço+(preço*20/100)))

#______________________________________________________________________________________________

#Desafio 45 Crie um programa que faça o computador jogar jokenpô com vc

from random import randint
print('Escolha sua opção:\n[0] Pedra \n[1] Papel \n[2] Tesoura')
itens=('Pedra', 'Papel', 'Tesoura')
computador=randint(0,2)
jogador=int(input('Sua Opção: '))
print('O computador escolheu {}'.format(itens [computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador==jogador:
    print('Empate')
elif computador == 0 and jogador == 2:
    print('Computador Ganhou')
elif computador == 1 and jogador == 0:
    print('Computador Ganhou')
elif computador == 2 and jogador == 1:
    print('Computador Ganhou')
else:
    print('Jogador Venceu')