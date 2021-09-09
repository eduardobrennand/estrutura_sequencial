#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

f = float(input('Temperatura em graus Fahrenheit: '))
c = 5 * ((f-32) / 9)
print('A temperatura de {:.2f} graus Fahrenheit eh igual a {:.2f} graus Celcius'.format(f, c))