'''
TIAGO VICTOR BANZE
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
fatorial=1
numero=int(input('Imprima uma numero : '))
for i in range(1,numero+1):
     fatorial=fatorial*i
    #  print(fatorial)
if numero==0:     
    print(f'FATORIAL de {numero} é igual a: {fatorial}')
else:
     print(f'FATORIAL de {numero} é igual a: {fatorial}')
