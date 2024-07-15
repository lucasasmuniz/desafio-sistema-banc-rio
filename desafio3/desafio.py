from abc import ABC, abstractmethod, abstractproperty
import datetime

class Historico():
    def __init__(self) -> None:
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({"tipo": transacao.__class__.__name__,"valor": transacao.valor,"data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),})

class Conta():
    def __init__(self,numero,cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor) -> bool:
        if valor < 0:
            print("Saque não realizado:\nValor solicitado para saque é inválido!")

        if self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado!")
            return True
        
        else:
            print("Saque não realizado:\nValor de saldo insuficiente!")
            return False

    def depositar(self, valor) -> bool:
        if valor < 0:
            print("Depósito não realizado:\nValor solicitado para depósito é inválido!")
            return False

        else: 
            self._saldo += valor
            print("Depósito")
            return True

    def __str__(self) -> str:
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
              """

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico,limite,limite_saques) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques

class Transacao(ABC):
    @abstractmethod
    def registrar(conta) -> None:
        pass

    @property
    @abstractproperty
    def valor(self):
        pass


class Saque(Transacao):
    def __init__(self,valor) -> float:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self,valor) -> float:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Cliente():
    def __init__(self,endereco) -> None:
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco,cpf,nome,data_nascimento) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento