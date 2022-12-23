#+ Adição 5+2==7
#- Subtração 5-2==3
#* Multiplicação 5*2==10
#/ Divisão 5/2==2.5
#** Potência 5**2==25
#// Divisão inteira 5//2==2
#% Resto da divisão 5%2==1

#Oredem de Precedência:
#1()
#2**
#3 * / // %
#4 + -

#pow(4,3)==64 

#nome=input('Qual é seu nome: ')
#print('Prazer em te conhecer {:20}!'.format(nome))

#{:20} significa 20 espaços :^20 significa que o nome vai ser centralizado em 20 espaços

#n1=int(input('Digite um Número:'))
#n2=int(input('Digite outro valor:'))
#s=n1 + n2
#m=n1 * n2
#d=n1 / n2
#di=n1 // n2
#e=n1 ** n2
#print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s,m,d))
#print('A divisão inteira {} e potência {}'.format(di,e))

#{:.2f} significa quantos números depois do . vai aparecer

#______________________________________________________________________________________________

#Desafio 05 Mostre o número inteiro, seu antecessor e sucessor
#n=int(input('Digite um Número:'))
#print ('O antecessor do numero {} é {} e seu sucessor é {}'.format(n, n-1, n+1))

#______________________________________________________________________________________________

#Desafio 06 leia um número e mostre o seu dobro, triplo e raiz quadrada
#n=int(input('Digite um número:'))
#print('O dobro do número {}, é {}. \nO triplo é {}. \nE a sua raiz quadrada é {:.2f}'.format(n,n*2,n*3,n**(1/2)))

#______________________________________________________________________________________________

#Desafio 07 leia as duas notas de um aluno, calcule e mostre a sua média 
#n1=float(input('Digite a primeira nota:'))
#n2=float(input('Insira a segunda nota:'))
#media=(n1+n2)/2
#print('A média final é {}'.format(media))

#______________________________________________________________________________________________

#Desafio 08 leia um valor em metros e exiba convertido em centímetros a milímetros
#n=float(input('Insira um número:'))
#cent=(n*100)
#mil=(n*1000)
#print('O valor {}, em centímetros é {:.2f}, e em milímetros é {:.2f}'.format(n,cent,mil))

#______________________________________________________________________________________________

#Desafio 09 leia um número qualquer e mostre na tela a sua tabuada
#n=int(input('Insira um número para tabuada:'))
#print('{} X {:2} = {}'.format(n,1,n*1))
#print('{} X {:2} = {}'.format(n,2,n*2))
#print('{} X {:2} = {}'.format(n,3,n*3))
#print('{} X {:2} = {}'.format(n,4,n*4))
#print('{} X {:2} = {}'.format(n,5,n*5))
#print('{} X {:2} = {}'.format(n,6,n*6))
#print('{} X {:2} = {}'.format(n,7,n*7))
#print('{} X {:2} = {}'.format(n,8,n*8))
#print('{} X {:2} = {}'.format(n,9,n*9))
#print('{} X {:2} = {}'.format(n,10,n*10))
#______________________________________________________________________________________________

#Desafio 10 leia quanto dinheiro ela tem na carteira e mostre quantos dólares ela pode comprar Considere 1 dólarR$3,27
din=float(input('Quanto dinheiro você tem na carteira? R$'))
dolar=din/3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(din,dolar))
#______________________________________________________________________________________________

#Desafio 11 leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la sabendo que cada litro de tintapinta uma área de 2m2

#______________________________________________________________________________________________

#Desafio 12 leia o preço de um produto e mostre seu novo preço com 5% de desconto

#______________________________________________________________________________________________

#Desafio 13 leia o salário de um funcionário e mostre seu novo salário com 15% de aumento