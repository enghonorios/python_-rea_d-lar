# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar 

n2= int(input(' QTD Notas de R$   2.00? '))
n5= int(input(' QTD Notas de R$   5.00? '))
n10= int(input('QTD Notas de R$  10.00? '))
n20= int(input('QTD Notas de R$  20.00? '))
n50= int(input('QTD Notas de R$  50.00? '))
n100=int(input('QTD Notas de R$ 100.00? '))

soma= (n2*2)+(n5*5)+(n10*10)+(n20*20)+(n50*50)+(n100*100)
dólar= soma/4.86

print(f'Valor total em sua carteira = {soma}')
print(f'Transformando real brasileiro para dólar = {dólar:.2f}')

#faça um programa que leia a largura e a altura de uma parede em metro, calcule a sua area e a quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma area de 2m2

p1= float(input('Largura da parede 1: '))
p11= float(input('Comprimento da parede 1: '))
p2= float(input('Largura da parede 2: '))
p22= float(input('Comprimento da parede 2: '))
pt= float(input('Largura e comprimento do teto: '))
Área= p1*p11+p2*p22+pt
Tintas= Área/18

print(f'Área total do quarto é igual: {Área} metros')
print(f'Será necessário {Tintas} latas de tintas para pintura.')
