"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

metros = float(input('Área a ser pintada, em metros quadrados: '))
litros = metros / 6
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)
preco_latas = latas * 80
precos_galoes = galoes * 25
mistura = (litros // 18) * 80 + (math.ceil(((litros % 18) / 3.6))* 25)

print(f'O preço utilizando-se apenas de latas é de: R${preco_latas}')
print(f'O preço utilizando-se apenas de galões é de: R${precos_galoes}')
print(f'O preço utilizando-se da mistura é de: R${mistura}')