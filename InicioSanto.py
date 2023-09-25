'''
TIAGO VICTOR BANZE
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o
nome "SANTO"
'''
cidade=input('Digite nome de uma Cidade com letras maúsculas: ').strip()
if cidade[0:5].upper()=='SANTO':
    print('A cidade digitada é', cidade)
else:
    print('a cidade digitada não tem nada de SANTO')    