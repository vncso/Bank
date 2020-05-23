class Pessoa:
    def __init__(self, nome, sobrenome, idade, cpf, renda):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
        self.renda = renda


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, idade, cpf, renda, tipo, senha):
        super().__init__(nome, sobrenome, idade, cpf, renda)
        self.__senha = senha
        if tipo == 'corrente':
            self.conta = ContaCorrente(100001, cpf, self.__senha)
        elif tipo == 'poupanca':
            self.conta = ContaPoupanca(100001, cpf, self.__senha)


class Conta(Cliente):
    def __init__(self,conta, cpf, senha, saldo=0, agencia=1):
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf
        self._saldo = saldo
        self.__senha = senha

    def sacar(self, senha, valor):
        if senha != self.__senha:
            print('Senha incorreta')
            return 0
        elif valor > self._saldo:
            print('Saldo insuficiente')
            return 0
        else:
            print(f'Saque de R${valor},00 efetuado com sucesso')
            self._saldo -= valor
            print(f'seu Saldo atual é de: R${self._saldo}')
            return self._saldo

    def _depositar(self, valor):
        if valor <= 0:
            print('Não foi possível realizar o depósito!')
            return 0
        else:
            self._saldo += valor
            print(f'depósito de R${valor},00 depositado com sucesso!')
            return self._saldo

    @property
    def saldo(self):
        return self._saldo * 2

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, 'str'):
            valor = float(valor.replace('R$', ''))
            self._saldo += valor
        else:
            self._saldo += float(valor)


class ContaCorrente(Conta, Cliente):
    def __init__(self,conta, cpf, senha, limite=0, saldo=0):
        super().__init__(conta, cpf, senha, saldo)
        self.limite = 500


    def sacar(self, senha, valor):
        if senha != self.__senha:
            print('Senha incorreta, operação cancelada')
            return 0
        elif valor > self._saldo + self.limite:
            print('Saldo insuficiente')
            return 0
        else:
            if valor > self._saldo:
                valor -= self._saldo
                self._saldo = 0
                self.limite -= valor
                print(f'foi utilizado R${valor} do seu limite de conta')
                print(f'saldo: {self._saldo}')
                print(f'limite: {self.limite}')
                return self._saldo
            else:
                self._saldo -= valor
                print(f'saldo: {self._saldo}')
                print(f'limite: {self.limite}')
                return self._saldo


class ContaPoupanca(Conta):
    def __init__(self, conta, cpf, senha, saldo=0):
        super().__init__(conta, cpf, senha, saldo)
