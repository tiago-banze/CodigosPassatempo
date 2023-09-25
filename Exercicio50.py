'''
TIAGO VICTOR BANZE
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidere-o
'''
soma=0
aux=0
cont=0
n1=int(input('DIGÍTE PRIMEIRO NÚMERO:\t'))
n2=int(input('DIGÍTE PRIMEIRO NÚMERO:\t'))
n3=int(input('DIGÍTE PRIMEIRO NÚMERO:\t'))
n4=int(input('DIGÍTE PRIMEIRO NÚMERO:\t'))
n5=int(input('DIGÍTE PRIMEIRO NÚMERO:\t'))
n6=int(input('DIGÍTE PRIMEIRO NÚMERO:\t'))
lista=[n1,n2,n3,n4,n5,n6]
for i in lista:
    if i%2==0 and i!=0:
        print(i)
        soma=i=i+aux
        aux=i
        cont+=1       
if cont==1:
    print(f'{cont} NÚMERO PAR INTRODUZIDO!\n\tA soma de número par introduzido é igual: {soma}')     
elif cont>1:
    print(f'{cont} NÚMEROS PARES INTRODUZIDOS!\n\tA soma dos números pares introduzidos é igual: {soma}')
else:
    print('Nenhum número introduzido é PAR!')
input('precione ENTER para sar')    
    
# if n1%2==0:
#     n1=n1
# else:
#     n1=0
# if n2%2==0:
#     n2=n2
# else:
#     n2=0        
# if n3%2==0:
#     n3=n3
# else:
#     n3=0        
# if n4%2==0:
#     n4=n4
# else:
#     n4=0        
# if n5%2==0:
#     n5=n5
# else:
#     n5=0        
# if n6%2==0:
#     n6=n6
# else:
#     n6=0        
# soma=n1+n2+n3+n4+n5+n6
# print(soma)        