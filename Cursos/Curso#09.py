#frase='Curso em Video Python'#A primeira letra começa do número 0
#frase[9:14] #vai do 9 ao 14
#frase[9:21:2] #vai do 9 ao 21 pulando de 2 em 2
#frase[:5] #vai do inicio até o 5
#frase[15:] #vai do 15 até o final
#frase[9::3]#vai começar do 9 e vai ate o final, porem ele pula de 3 em 3 
#len(frase) =comprimento da frase
#frase.count('o') #contar quantas vezes aparece o 'o'
#frase.find('deo') #indica a posição que se encontra
#'Curso' in frase #pergunta se existe 'Curso' na frase
#frase.replace('Python','Android') #aonde estiver escrito python ele vai substituir por android
#frase.upper() #ele pega todas as letras minúsculas e transforma em maiúsculas
#frase.lower() #transforma todas as letras em minúsculas
#frase.capitalize #ele pega todas as letras coloca em minúsculas e somente a primeira em maiúscula
#frase.title() #vai analisar quantas palavras existem
#frase.strip() #vai remover todos os espaços inúteis
#frase.rstrip() #ele vai remover os espaços da direira
#frase.lstrip() #ele vai remover os espaços da esquerda
#frase.split() #ele vai pegar aonde tem espaços e fazer uma divisão ou seja ele pega as palavras separa e cria uma outra lista
#'-'.join(frase) #ele vai juntar todas as palavras e vai separar com -

#frase='Curso em Video Python'
#print(frase[1:15:2])

#frase='Curso em Video Python'
#print(frase.count('o'))

#frase='Curso em Video Python'
#print('Curso' in frase)

#______________________________________________________________________________________________

#Desafio22 Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúsculas
#o nome com todas as letra minúsculas
#quantas letras ao todo(sem considerar espaços)
#quantas letras tem o primeiro nome

nome=str(input('insira seu nome:')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em maiúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) 



#______________________________________________________________________________________________

#Desafio23 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados 
#ex: entrada: digite um número:1834
#saida: unidade:4
#       dezena:3
#       centena:8
#       milhar:1
num=int(input('informe um número: '))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('Unidade {}'.format(u))
print('Dezena  {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))


#______________________________________________________________________________________________

#Desafio24 Crie  um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

cid=str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO') #SANTO tem 5 letras [:5]

#______________________________________________________________________________________________

#Desafio25 Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
nome=str(input('Qual é seu nome? ')).strip()
print('Seu nome tem Silva?'.format('SILVA' in nome.upper())) 

#______________________________________________________________________________________________

#Desafio26 Faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra 'A'
#em que posição ela aparece pela primeira vez
#em que posição aparece pela última vez

frase=str(input('Qual é sua frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))



#______________________________________________________________________________________________

#Desafio27 Faça um programa que leia o nome completo de um pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente.
#entrada:ana maria de souza
#saida: primeiro=ana
#       último=souza

nome=str(input('Digite seu nome completo: ')).strip()
n=nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))

