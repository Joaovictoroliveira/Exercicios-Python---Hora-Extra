n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 and n1 > n3:
    print(n1, 'e maior que',n2, 'e',n3 )
elif n2 > n1 and n2 > n3:
    print(n2, 'e maior que',n1, 'e',n3)
elif n3 > n1 and n3 > n2:
    print(n3, 'e maior que',n1, 'e',n2)
else:
    print('Os numeros sao iguais')
