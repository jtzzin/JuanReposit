import hashlib

class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha =  self.hash_senha(senha)
        self.__ativo = False

    def hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def set_nome(self, nome):
        self.__nome = nome 
    
    def get_nome(self):
        return self.__nome
    
    def set_email(self, email):
        self.__email = email
    
    def get_email(self):
        return self.email
    
    def ativar(self):
        self.__ativo = True
        print(f"Usuario {self.nome} foi ativado")

    def get_senha(self):
        return self.__senha
    
    def verifica_senha(self, senha):
        return self.__senha == self.hash_senha(senha=)

    def alterar_senha_usuario(self, senha_antiga, senha_nova):
        if self.verifica_senha(senha_antiga):
            self.__senha = self.hash_senha(senha_nova)
            print(f"sua senha foia mlterada")

    def detalhes_usuario
        print(f'nome: {self.__nome}')
        print(f'email: {self.__email}')
        print(f'ativo: {self.__ativo}')
        print(f'senha {self.__senha}')
    
    def desativar (self): 
        self.__ativo = False 
        print(f"Usuario {self.nome} foi desativado")

    def get_ativo(self):
        return self.__ativo
    
    def detalhes_usuario(self):
        print(f'nome: {self.__nome}')
        print(f'email: {self.__email}')
        print(f'ativo: {self.__ativo}')
    
    
user1 = Usuario("Terebentina Teles", "tere@mail.com.br", "123456")

try:
    print(user1.__nome)
except AttributeError as e:
    print(f'Erro: {e}')

print(user1.get_nome())


