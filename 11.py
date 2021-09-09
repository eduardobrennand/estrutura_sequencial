"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a)o produto do dobro do primeiro com metade do segundo .
b)a soma do triplo do primeiro com o terceiro.
c)o terceiro elevado ao cubo."""

n1 = int(input('Primeiro numero inteiro: '))
n2 = int(input('Segundo numero inteiro: '))
n3 = float(input('Numero real: '))

a = (n1 * 2) * (n2 / 2)
b = (n1 * 3) + n3
c = n3 ** 3

print('O resultado da letra A: {}'.format(a))
print('O resultado da letra B: {}'.format(b))
print('O resultado da letra C: {}'.format(c))