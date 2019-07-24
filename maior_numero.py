n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(n1, 'e maior que ', n2)
elif n2 > n1:
    print(n2, 'e maior que ', n1)
else:
    print('Os numeros sao iguais')
