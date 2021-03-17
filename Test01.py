q1 = float(input('Digite a quantidade da primeira compra:'))
v1 = float(input('Digite o valor da primeira compra: R$'))
q2 = float(input('Digite a quantidade da segunda compra:'))
v2 = float(input('Digite o valor da segunda compra: R$'))
m1 = q1 * v1
m2 = q2 * v2
pm = (m1+m2)/(q1+q2)
print('O preço medio é R${:.2f}'.format(pm))