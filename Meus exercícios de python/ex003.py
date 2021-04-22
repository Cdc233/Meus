#Crie um programa que leia dois números e mostre a soma entre eles

a1 = float(input('Digite um número: '))
a2 = float(input('Digite outro número: '))

print(f'A soma entre {a1:.0f} e {a2:.0f} é {a1 + a2:.0f}')
#modo 2 otimizado
v = 0
for c in range (0, 2):
    a = float(input('Digite um número: '))
    v += a 
print(f'A soma entre eles é de {v} ')  