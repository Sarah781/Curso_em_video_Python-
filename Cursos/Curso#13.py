#for c in range(1,10): ->significa fazer o contador c no intervalo de 1 até 10


#______________________________________________________________________________________________

#n=int(input('Insira um número para tabuada: '))
#for c in range (0,11):
#    print ('{}x{}={}'.format(n,c,n*c))
#print ('Fim')

#______________________________________________________________________________________________

#Desafio 46 Faça um programa que mostre na tela uma contagem regressiva para os fogos de artifício indo de 10 
#até 0, com uma pausa de 1 segundo entre eles.

import time

for t in range(10, 0, -1):
    print(t)
    time.sleep(1)

print("Feliz Ano Novo! Feliz 2023!")


#______________________________________________________________________________________________

#Desafio 47 Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for i in range(1, 51):
    if i % 2 == 0: #se o resto da divisão for 0 o programa imprime o i
        print(i)

#______________________________________________________________________________________________

#Desafio 48 Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se
#encontram no intervalo de 1 até 500

soma = 0                          # Inicializa a variavel soma
for c in range(1, 501):           # Para cada valor de c no intervalo de 1 até 500
    if c % 2 != 0 and c % 3 == 0: # Se for impar e divisivel por 3
        soma += c                 # Soma o valor de c em soma. Equivalente: soma = soma + c
print(soma)                       # Escreve o valor de soma na tela

#______________________________________________________________________________________________

#Desafio 49 Refaça o desafio 9 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando 
#um laço for

n=int(input('Insira um número para tabuada: '))
for c in range (0,11):
    print ('{}x{}={}'.format(n,c,n*c))

#______________________________________________________________________________________________

#Desafio 50 Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares
#Se o valor digitado for ímpar, desconsidere-o

soma = 0
for c in range(6):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        soma += numero
print(soma)


#______________________________________________________________________________________________

#Desafio 51 Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 
#primeiros termos dessa progressão

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
for i in range(10):
    print(primeiro_termo)
    primeiro_termo += razao

#______________________________________________________________________________________________

#Desafio 52 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

primo = True
numero = int(input('Digite um numero: '))
for divisor in range(2, numero):
     if numero % divisor == 0:
         primo = False
print('{} eh primo: {}'.format(numero, primo))

#______________________________________________________________________________________________

#Desafio 53 Crie um programa que leia uma frase qualquer e diaga se ela é um palíndromo, desconsiderando os espaços

# Obtenha a frase do usuário
frase = input("Digite uma frase: ")

# Remova os espaços da frase
frase_sem_espacos = frase.replace(" ", "")

# Verifique se a frase é um palíndromo
if frase_sem_espacos == frase_sem_espacos[::-1]:
  # A frase é um palíndromo
  print("A frase é um palíndromo")
else:
  # A frase não é um palíndromo
  print("A frase não é um palíndromo")


#______________________________________________________________________________________________

#Desafio 54 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
#ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
idade_minima = 18
maiores = 0
menores = 0
for c in range (7):
  ano=int(input('Insira o ano de nascimento: '))
  idade=date.today().year - ano
  if idade >= idade_minima:
    maiores += 1
  else:
    menores += 1

#print('Maiores de idade: {}'.format(maiores))
#print('Menores de idade: {}'.format(menores))

#______________________________________________________________________________________________

#Desafio 55 Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido

maior = float(input('Peso: kg ')) #Isso significa que, inicialmente, o maior peso lido é também o menor peso lido.
menor = maior

for i in range(4):
  peso = float(input('Peso: kg '))

  if peso > maior:
    maior = peso

  if peso < menor:
    menor = peso

print('O maior peso lido foi {}, O menor peso lido foi {}'.format(maior, menor))



#______________________________________________________________________________________________

#Desafio 56 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#a média de idade do grupo
#qual é o nome do homem mais velho
#quantas mulheres têm menos de 20 anos
