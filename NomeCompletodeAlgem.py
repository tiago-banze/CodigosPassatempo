'''
TIAGO VICTOR BANZE
Crie um programa que leia nome completo de uma pessoa e mostre.
->O nome com todas as letras maíusculas;
->O nome com todas as letras minúsculas;
->O nome com as inicias maíusculas;
->Quantas letrs ao todo (sem considerar espaços);
->Quantas letras tem o primeiro nome.
'''
nome=input('Imprima o teu nome: ')
maiu=nome.upper()
minu=nome.lower()
inicialMaiu=nome.title()
letra=nome.split()
juntar=len(''.join(letra))
print(f'{nome} tem {juntar} letras')
print(f'\nO teu nome a Maíuscula é: {maiu}')
print(f'\nO teu nome a Minúsculas é: {minu}')
print(f'\nO teu nome organizado é: {inicialMaiu}')
print(f'\n{letra[0]} tem {len(letra[0])} letras')
print(dir(nome))
print(len(dir(nome)))
