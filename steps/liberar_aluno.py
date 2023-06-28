from behave import when, then
from refeitorio import *


@when("a probabilidade de liberacao for {probabilidade} porcento")
def when_probabilidade_de_liberacao(context, probabilidade):
    context. total_de_alunos_liberados = liberar_alunos(
        context.alunos_reconhecidos, int(probabilidade))


@then("pelo menos, um(a) aluno deve ser liberado")
def then_alunos_liberados(context):
    assert context.total_de_alunos_liberados > 0
