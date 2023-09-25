'''
TIAGO VICTOR BANZE
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
'''
resposta=1
while resposta==1:
    numero=int(input('Dígite o numero que desejas saber se é PAR ou IMPAR:\n\t'))
    print(numero)
    if numero%2==0:
        print(f'{numero} é PAR')
    else:
        print(f'{numero} é IMPAR')
    resposta=int(input('deseja continuar:')   ) 