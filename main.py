from desafios.bank.classes import *

print('Seja bem vindo ao VNBank!')
print('O que deseja fazer?')
print()
print('1 - Abrir Conta corrente')
print('2 - Abrir Conta Poupança')
print('3 - Acessar minha conta')
opcao = input('Digite a opção desejada: ')

if int(opcao) == 1:
    print('Abria a conta é rápido e fácil, basta responder as perguntas:')
    nome = input('Qual é seu primeiro nome? ')
    sobrenome = input(f'{nome}, qual é seu sobrenome? ')
    idade = input('E quantos anos você tem? ')
    cpf = input(f'{nome}, precisamos saber o seu CPF: ')
    renda = input(f'Qual é a sua renda, {nome}? ')
    senha = input(f'{nome}, digite uma senha numérica para sua conta: ')

    c1 = Cliente(nome, sobrenome, idade, cpf, renda, 'corrente', senha)

elif int(opcao) == 2:
    print('Abria a conta é rápido e fácil, basta responder as perguntas:')
    nome = input('Qual é seu primeiro nome? ')
    sobrenome = input(f'{nome}, qual é seu sobrenome? ')
    idade = input('E quantos anos você tem? ')
    cpf = input(f'{nome}, precisamos saber o seu CPF: ')
    renda = input(f'Qual é a sua renda, {nome}? ')
    senha = input(f'{nome}, digite uma senha numérica para sua conta: ')

    c1 = Cliente(nome, sobrenome, idade, cpf, renda, 'poupanca', senha)

else:
    print('opcao inválida!')


operacao = 0
while operacao != 4:
    print(f'{c1.nome}, o que deseja fazer?')
    print()
    print('1 - consultar saldo')
    print('2 - Sacar um valor')
    print('3 - Depositar um valor')
    print('4 - sair')

    operacao = input('informe a opção desejada: ')

    if int(operacao) == 1:
        print(c1.conta._saldo)

    elif int(operacao) == 2:
        valor = float(input(f'{c1.nome}, qual valor deseja sacar? '))
        senha = input('informe sua senha: ')
        c1.conta.sacar(senha, valor)

    elif int(operacao) == 3:
        valor = float(input(f'{c1.nome}, informe o valor que será depositado: '))
        c1.conta._depositar(valor)
    else:
        print('operação inválida')