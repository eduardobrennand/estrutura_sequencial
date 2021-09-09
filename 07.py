#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

l = int(input('Digite o lado do quadrado: '))
area = l ** 2
dobro = area * 2
print('A area do quadrado eh de {} e o dobro da area eh {}'.format(area, dobro))