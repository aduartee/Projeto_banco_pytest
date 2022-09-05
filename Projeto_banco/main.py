from Projeto_banco.Projeto import Employer


def test_idade():
    funcionario_teste = Employer("Arthur", "02/03/2002", 100000)
    print(f'Teste = {funcionario_teste.decrescimo_salario()}')

