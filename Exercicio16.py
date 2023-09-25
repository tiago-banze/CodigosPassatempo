'''
TIAGO VICTOR BANZE
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
porção inteira. Exemplo: o número 6,127 tem a parte inteira 6.
'''
numero=float(input('...: '))
# print(int(numero))%8.2f
print(f"Á porção inteira de {numero:.0f} é: {int(numero)} ")