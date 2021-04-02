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
novoq1 = q1 + q2
pm1 = pm
novom1 = novoq1 * pm1
novom2 = q2 * v2
pm2 = (novom1+novom2)/(novoq1+q2)
qtotal1 = novoq1 + q2
opção = 0
while opção != 4:
    print('''    
    [ 1 ] Mostrar preço médio
    [ 2 ] Calcular outro preço médio
    [ 3 ] Continuar calculando
    [ 4 ] Sair
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
        print('A quantidade total é {:.4f} com preço medio de R${:.4f}'.format(novoq1, pm1))
        q2 = float(input('Digite outra quantidade:'))
        v2 = float(input('Digite outro valor: R$'))
        print('A quantidade total é {:.4f} com preço medio de R${:.4f}'.format(qtotal1, pm2))
    elif opção == 4:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(4)
print('Fim do programa!')


