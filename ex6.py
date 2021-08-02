#6. Faça um programa que mostre a soma de dois valores, e depois mostre o antecessor e o sucessor do mesmo.
num = int(input('Digite um número inteiro:'))
sucessor = num + 1
antecessor = num - 1
print('O número escolhido foi {}, seu sucessor é o {}, e o antecessor é o {}.'.format(num, sucessor, antecessor))