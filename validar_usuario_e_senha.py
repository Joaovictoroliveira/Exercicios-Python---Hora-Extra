usuario = senha = ' '
while(usuario == senha):
    usuario = input('Digite o nome do usuario: ')
    senha = input('Digite a senha: ')
    if(usuario == senha):
        print('O usuario nao pode ser igual senha')
