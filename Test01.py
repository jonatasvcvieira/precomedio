q1 = float(input('Digite a quantidade da primeira compra:'))
v1 = float(input('Digite o valor da primeira compra: R$'))
q2 = float(input('Digite a quantidade da segunda compra:'))
v2 = float(input('Digite o valor da segunda compra: R$'))
m1 = q1 * v1
m2 = q2 * v2
pm = (m1+m2)/(q1+q2)
novoq1 = q1 + q2
novov1 = pm
while
opção = str(input('Deseja calcular mais um preço médio? [S/N] ')).strip().upper()[0]
    opção = str(input(''))

print('O preço medio é R${:.2f}'.format(pm))
print('Agora você tem {} com preço médio de {:.2f}'.format(novoq1, novov1))
