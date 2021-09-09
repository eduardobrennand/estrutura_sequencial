#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
import math

mb = float(input('Tamanho do arquivo para download em MB: '))
internet = int(input('Velocidade da Internet em Mbps: '))
download = mb / internet

print(f'O tempo aproximado de download de um arquivo de {mb}MBs em uma internet com a velocidade de {internet}Mb/s é de {download} segundo(s), ou {(download / 60)} minutos.')
