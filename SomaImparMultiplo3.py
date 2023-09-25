'''
TIAGO VICTOR BANZE
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
de três e que se encontram no intervalo de 1 até 500.
'''
aux=0
soma=0
for i in range(1,501):
    if i%2!=0 and i%3==0:
        soma=i=i+aux
        aux=i
print(f'A soma de todos números Ímpares e múltiplos de 3 que estão no intervalo de 1-500 é igual a: {soma}')