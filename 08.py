#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = int(input('Qual o valor da hora? '))
horas_mes = int(input('Quantas horas por mes? '))
salario = valor_hora * horas_mes
print(f'Seu salario mensal eh de R${salario}')