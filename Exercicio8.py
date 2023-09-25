'''
TIAGO VICTOR BANZE
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
e milímetros.
'''
print('programa que recebe um valor em metro\n')
metro=float(input('IMPRIMA O UM VALOR EM METROS:\t'))

centimetro=metro*100
milimetro=metro*(100*10)
if metro==1:
    print(f'{metro} metro equivale a {centimetro} centímetros.\n{metro} metro equivale a {milimetro} milímetros.')
elif metro==0:
    print(f'{metro} metro equivale a {centimetro} centímetro.\n{metro} metro equivale a {milimetro} milímetro.')
else:
    print(f'{metro} metros equivale a {centimetro} centímetros.\n{metro} metro equivale a {milimetro} milímetros.')