'''
TIAGO VICTOR BANZE
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
 '''
print('TABUADA')
numero=int(input('IMPRIMA O NUMERO QUE DESEJA SABER A SUA TABUADA:\t'))
i=1
print('\t\t',numero)
while i<=12: 
    print(numero,'*',i,'=',i*numero)
    i+=1
    