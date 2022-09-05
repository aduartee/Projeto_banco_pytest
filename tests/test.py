import pytest
from pytest import mark
from Projeto_banco.Projeto import Employer

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '16/02/2000'  # Given
        esperado = 22

        funcionario_teste = Employer('Teste', entrada, 1111)
        result = funcionario_teste.idade()  # When

        assert result == esperado  # Then

    def test_quando_sobrenome_recebe_Arthur_Duarte_deve_retornar_Duarte(self):
        entrada = 'Arthur Duarte'
        esperado = 'Duarte'

        arthur = Employer(entrada, '11/11/2000', 10000)

        result = arthur.sobrenome()
        assert result == esperado


    def test_quando_decrecimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Employer(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()  # When
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000000

            funcionario = Employer('Joao', '06/10/2005', entrada)
            resultado = funcionario.calcular_bonus()
            assert resultado

