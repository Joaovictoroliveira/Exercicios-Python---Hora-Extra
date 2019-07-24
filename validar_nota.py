nota = - 1
while (nota < 0) or (nota > 10):
    nota = int(input('Digite uma nota: '))
    if (nota < 0) or (nota > 10):
        print('Nota invalida')
    else:
        print(nota, 'e uma nota valida')
