while 1:
    nome=input('digite o seu nome completo: ').strip().title()
    '''
    a=''
    b=''
    for i in range(len(nome)):
        a=a+nome[i]
        if nome[i]==' ':
            break
    for j in range(len(nome)):
        b=b+nome[::-1]
    aux=b
    aux2= ''
    for ii in range(len(aux)):
        aux2=aux2+aux[ii]
        if nome[ii]==' ':
            break
    print(f'primeiro nome é {a} e último nome é {aux2[::-1]}\n')
    ''' 

    nome2=nome.split()
    nome2inv=nome2[::-1]
    print(f'seu primeiro nome é {nome2[0]}\nseu último nome é {nome2inv[0]} \n')
    input("Clique ENTER para sair do programa.")
    break
