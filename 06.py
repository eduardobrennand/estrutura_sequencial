#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

r = float(input('Qual o raio do circulo? '))
area = math.pi * r**2
print('O valor da area do circulo desejado eh de {:.2f}'.format(area))