'''
TIAGO VICTOR BANZE
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M"ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto
'''
genero=input('Imprima o seu genero, "M"masculino e "F" para femenino:\n\t')
while genero !='M' or genero != 'F':
   genero=input('\nPorfavor imprima "M" or "F":\t') 
   if genero=='M' or genero=='F':
      break

if genero=='M':
    print('O teu genero é MASCULINO')
if genero =='F':
    print('O teu genero é FEMENINO')   

# while 1:
#    genero=input('Imprima o seu genero, "M"masculino e "F" para femenino:\n\t')
#    if genero !='M' or genero != 'F':
#         genero=input('\nPorfavor imprima "M" or "F":\t') 
#    elif genero=='M' or genero=='F':
#       break

# if genero=='M':
#     print('O teu genero é MASCULINO')
# if genero =='F':
#     print('O teu genero é FEMENINO')   
