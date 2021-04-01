from time import sleep
print('**** PREÇO MÉDIO ****')
print('=-=' * 7)
sleep(2)
q1 = float(input('Digite a quantidade da primeira compra:'))
v1 = float(input('Digite o valor da primeira compra: R$'))
q2 = float(input('Digite a quantidade da segunda compra:'))
v2 = float(input('Digite o valor da segunda compra: R$'))
m1 = q1 * v1
m2 = q2 * v2
pm = (m1+m2)/(q1+q2)
opção = 0
while opção != 3:
    print('''    
    [ 1 ] Mostrar preço médio
    [ 2 ] Calcular outro preço médio
    [ 3 ] Sair
    ''')
    opção = int(input('>>>>> Qual é a sua opção?'))
    if opção == 1:
        m1 = q1 * v1
        m2 = q2 * v2
        qtotal = q1 + q2
        pm = (m1 + m2) / (q1 + q2)
        print('=-=' * 10)
        print('A quantidade total é {:.4f} com preço medio de R${:.4f}'.format(qtotal, pm))
    elif opção == 2:
        print('Informe os valores novamente:')
        q1 = float(input('Digite a quantidade da primeira compra:'))
        v1 = float(input('Digite o valor da primeira compra: R$'))
        q2 = float(input('Digite a quantidade da segunda compra:'))
        v2 = float(input('Digite o valor da segunda compra: R$'))
    elif opção == 3:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(4)
print('Fim do programa!')


