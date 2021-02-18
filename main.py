"""
Validador de CNPJ
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0  4  2  5  2  0  1  1  0  0  0  1  X  X
5  4  3  2  9  8  7  6  5  4  3  2
0  16 6  10 18 0  7  6  0  0  0  2 = 65 ##

Fórmula -> 11 - (65 % 11) = 1
Primeiro dígito = 1

0  4  2  5  2  0  1  1  0  0  0  1  1  X
6  5  4  3  2  9  8  7  6  5  4  3  2
0  20 8  15 4  0  8  7  0  0  0  3  2 = 67 ##
Fórmula -> 11 - (67 % 11) = 11 (Como o resultado é maior que 9, então é 0)
Segundo dígito = 0

Novo CNPJ + Dígitos = 04.252.011/0001-10
CNPJ original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro dígito
6543298765432 -> Segundo dígito
"""
import cnpj
from random import randint
# O número de CNPJ inicia com 8 dígitos centrais que chamamos aqui de numero_parte1
# o numero_parte2 indica se aquele CNPJ é de uma matriz ou filial, sendo incrementado por 1.
# por exemplo, 0001 = matriz. 0002 = filial 1. 0003 = filial 2, etc. Portanto, geramos a segunda parte de forma diferente.
numero_parte1 = randint(10000000, 99999999)
numero_parte2 = randint(1, 10)

if numero_parte2 < 10:
    numero_parte2 = '000' + str(numero_parte2)
else:
    numero_parte2 = '00' + str(numero_parte2)

cnpj_base = str(numero_parte1) + numero_parte2

# print(numero_parte2)
# print(cnpj_base)

cnpj_final = cnpj.calcular_digitos(cnpj_base)
print(f'CNPJ Gerado: {cnpj_final}')


