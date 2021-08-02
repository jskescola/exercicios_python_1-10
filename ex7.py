#7. Leia um número, mostre seu dobro, triplo, e raíz quadrada.
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizQuadrada = pow(num, 1/2)

print('O dobro de {} é {}, o triplo é {}, e a raíz quadrada é {}.'.format(num, dobro, triplo, raizQuadrada))