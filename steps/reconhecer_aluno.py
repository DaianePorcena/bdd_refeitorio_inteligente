from behave import given, when, then
from refeitorio import *

@given("o ambiente de desenvolvimento esteja preparado corretamente")
def given_ambiente_preparado_corretamente(context):
    preparado, context.configuracao = preparar()

    assert preparado

@when("a foto {foto} de pessoas for capturada")
def when_foto_de_pessoas_capturada(context, foto):
    context.pessoas = simular_entradas(foto)

    assert context.pessoas is not None

@then("pelo menos, um(a) aluno deve ser reconhecido")
def then_um_aluno_reconhecido(context):
    alunos_reconhecidos, context.alunos_cadastrados = reconhecer_alunos(context.configuracao, context.pessoas)
    
    assert alunos_reconhecidos

@then("nenhum(a) aluno deve ser reconhecido")
def then_nenhum_aluno_reconhecido(context):
    alunos_reconhecidos, _ = reconhecer_alunos(context.configuracao, context.pessoas)

    assert not alunos_reconhecidos

@then("{total_de_reconhecimentos} alunos devem ser reconhecidos")
def then_total_de_alunos_reconhecidos(context, total_de_reconhecimentos):
    _, context.alunos_cadastrados = reconhecer_alunos(context.configuracao, context.pessoas)

    assert len(context.pacientes) == int(total_de_reconhecimentos)