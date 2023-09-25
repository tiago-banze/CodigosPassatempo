'''
TIAGO VICTOR BANZE
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma Sequência de Fibonacci.
'''
numero=int(input('Imprima o numero que deseja saber a sequência de fibonacci:'))
a1=1
a2=0
aux=0
for i in range(1,numero+1):
    print(a1)
    aux=a1
    a1+=a2
    a2=aux
