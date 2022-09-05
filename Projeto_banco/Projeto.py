from datetime import date


class Employer:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def sobrenome(self):
        nome_comepleto = self._nome.strip()
        nome_separado = self._nome.split(' ')
        return nome_separado[-1]

    # Calculo data de nascimento
    def idade(self):
        data_nascimento = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 10000:
            raise Exception('O valor é muito alto para receber um bonus')
        return valor

    def _socios(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self._salario >= 100000 and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        if self._socios():
            decrescimo = self.salario * 0.1
            self._salario -= decrescimo

    def __str__(self):
        return f" O Funcionario {self.nome}, {self._data_nascimento}, {self._salario}"
