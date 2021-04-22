#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

while True:
   a = int(input('Digite um número: '))

   print(f'O antecessor de {a} é {a-1} e o sucessor é {a+1}')

   b = input('Deseja continuar?[S/N]: ')

   if b in 'Nn':
      break
