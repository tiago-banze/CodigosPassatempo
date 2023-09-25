nome = input('digite o nome do produto: ')
valor_pagar = float(input('digite o valor do produto: '))
quant = int(input('digite a quantidade do produto: '))
resposta=0
lista_nome=[nome]
lista_valor=[valor_pagar]
lista_quant=[quant]
resposta=int(input('deseja continuar?'))

while True:
    nome = input('digite o nome do produto: ')
    valor_pagar = int(input('digite o valor do produto: '))
    quant = int(input('digite a quantidade do produto: '))
    lista_nome.append(nome)
    lista_valor.append(valor_pagar)
    lista_quant.append(lista_quant)
    resposta=int(input('deseja continuar?'))
    if resposta ==0:
        break
        
for i in range(len(lista_quant)+1):
    print(f'produto: {lista_nome[i]}\npreço : {lista_valor[i]}\nquantidade: {lista_quant[i]}\nO preço a pagar{lista_valor[i]*lista_quant[i]} \n____________________')
    
# print(lista_nome)
# print(lista_quant)
# print(lista_quant)        
# print(f'nome do produto: {nome}\nvalor do produto: {valor_pagar}\nquantidade do produto: {quant}')