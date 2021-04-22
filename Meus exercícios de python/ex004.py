#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

b = input('Digite algo: ')

if len(b) > 1:
    print(f'{b} tem {len(b)} caracteres')
elif len(b) == 1:
    print(f'{b} tem 1 caracter')