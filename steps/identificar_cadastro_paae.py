from behave import when, then
from refeitorio import *

@when("um cadastro for identificado")
def identificar_cadastro_paae(context):
    context.total_de_alunos_cadastrados = identificar_cadastro_paae(context.alunos_reconhecidos)
    
@then("pelo menos, um(a) terá o acesso ao refeitório")
def identificar_cadastro_paae(context):
    assert context.total_de_alunos_cadastrados > 0
    