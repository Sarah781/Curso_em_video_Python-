#bibliotecas
#import math 
#from math import sqrt (para apenas selecionar uma das funcionalidades)
#ceil arredonda para cima 
# floor arredonda para baixo
#trunc tira os números depois do ponto
#pow faz a função dos **
#sqrt calculo de raiz quadrada
#factorial cálculo de fatorial de um número

import emoji
  
print(emoji.emojize(":grinning_face_with_big_eyes:"))


#Desafio 16 leia um numero real qualquer pelo teclado e mostre a sua porção inteira 
# ex:6127 sua porção inteira é 6
import math
num=float(input('insira um número:'))
print('sua proção inteira é:{}'.format(math.trunc(num)))

#Desafio 17 leia o cumprimento de cateto oposto e do catedo adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa.
import math
cat_oposto=float(input('Insira o comprimento do cateto oposto:'))
cat_adja=float(input('insira o comprimento do cateto adjacente:'))
h= (cat_oposto**2+cat_adja**2)**(1/2)
print('a hipotenusa é = {:.2f}'.format(h))

#Desafio 18 leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo=float(input('Digite o ângulo que vc deseja:'))
seno=math.sin(math.radians(angulo))
cos=math.cos(math.radians(angulo))
tang=math.tan(math.radians(angulo))
print('o angulo {}, corresponde a \nseno {:.2f} \ncosseno {:.2f} \ntangente {:.2f#}'.format(angulo,seno,cos,tang))

#Desafio 19 um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido sort
from random import choice
aluno1=str(input('Aluno 1:'))
aluno2=str(input('Aluno 2:'))
aluno3=str(input('Aluno 3:'))
aluno4=str(input('Aluno 4:'))
lista=[aluno1,aluno2,aluno3,aluno4]
escolhido= choice(lista)
print('O aluno sorteado foi: {}'.format(escolhido))

#Desafio 20 o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
aluno1=str(input('Aluno 1:'))
aluno2=str(input('Aluno 2:'))
aluno3=str(input('Aluno 3:'))
aluno4=str(input('Aluno 4:'))
lista=[aluno1,aluno2,aluno3,aluno4]
escolhido=shuffle(lista)
print('a ordem de apresentação será: {}'.format(lista))


#Desafio 21 faça um programa em python que abra e reproduza o áudio de um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()