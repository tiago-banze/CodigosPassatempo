'''
TIAGO VICTOR BANZE
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
'''
numero=0
numero2=0
numero3=0
resposta='Sim'
while resposta=='Sim':
    numero=int(input('disque primero numero: '))
    numero2=int(input('disque segundo numero: '))
    numero3=int(input('disque terceiro numero: '))
    print(f'n1={numero}\nn2={numero2}\nn3={numero3}\n')
    if numero>numero2 and numero>numero3:
        print(f'{numero} é maior de todos')
    elif numero2>numero and numero2>numero3:
        print(f'{numero2} é maior de todos')
    else :
        print(f'{numero3} é maior de todos')
    resposta=input("deseja continuar?\nDisque 'Sim' se sim:")
