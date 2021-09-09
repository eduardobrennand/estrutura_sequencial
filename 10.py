#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = float(input('Digite a temperatura em graus Celcius: '))
f = (9 * c) / 5 + 32
print('A temperatura de {:.2f} graus Celcius eh igual a {:.2f} graus Fahrenheit'.format(c, f))
