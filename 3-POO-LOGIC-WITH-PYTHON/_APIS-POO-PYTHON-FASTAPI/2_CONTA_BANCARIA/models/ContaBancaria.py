from abc import ABC, abstractmethod


class ContaBancaria(ABC):
    def __init__(self, numero_conta:int, nome_titular:str, saldo:float = 0):
        self._numero_conta = numero_conta
        self._nome_titular = nome_titular
        self.__saldo = saldo
    
    def get_numero_conta(self):
        return self._numero_conta
    
    def get_nome_titular(self):
        return self._nome_titular
    
    def set_nome_titular(self, novo_nome: str):
        self._nome_titular = novo_nome
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, novo_saldo: float):
        self.__saldo = novo_saldo
        
    @abstractmethod
    def depositar(self):
        pass
    
    @abstractmethod
    def sacar(self):
        pass