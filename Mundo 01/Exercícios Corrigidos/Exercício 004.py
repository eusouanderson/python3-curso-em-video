"""
EXERCÍCIO 004: Dissecando uma Variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""
'''a = input('Digite algo: ')
print('O tipo primitivo deste valor é: {}'.format(type(a)))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está em maiúsculas? {}'.format(a.isupper()))
print('Está em minúsculas? {}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))'''
def primit(a=''):
    a = a
    print(f'{a.isspace()}')
    print(f'{a.isnumeric()}')
    print(f'{a.isalpha()}')
    print(f'{a.isalnum()}')
    print(f'{a.isupper()}')
    print(f'{a.islower()}')
    print(f'{a.istitle()}')

primit('884545 888')