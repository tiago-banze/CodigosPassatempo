resposta='Sim'
while resposta=='Sim':
    numero=int(input('disque primero numero: '))
    print(f'Tabuada de {numero}')
    for i in range(13):
        multiplicacao=i*numero
        print(f'\t{i}*{numero}={multiplicacao}')

    resposta=input("deseja continuar?\nDisque 'Sim' se sim:")