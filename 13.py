"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 
"""

altura = float(input('Digite a altura, em metros: '))
h = (72.7 * altura) - 58
m = (62.1 * altura) - 44.7
print('O peso ideal masculino é de {:.2f} e o peso ideal feminino é de {:.2f}'.format(h, m))

