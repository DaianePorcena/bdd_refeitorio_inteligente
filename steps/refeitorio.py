import face_recognition as reconhecedor
import colored
import random
import json


ARQUIVO_DE_CONFIGURACAO = "/home/daiane/Área de Trabalho/Faculdade/IHM/refeitorio_inteligente/bdd_refeitorio_inteligente/configuracao.json"

# ler configuracoes e preparar estruturas de dados


def preparar():
    preparado, configuracao = False, None

    try:
        with open(ARQUIVO_DE_CONFIGURACAO, "r") as arquivo:
            configuracao = json.load(arquivo)
            if configuracao:
                print("arquivo de configuracao carregado")
            arquivo.close()

            preparado = True
    except Exception as e:
        print(f"erro lendo configuração: {str(e)}")

    return preparado, configuracao


def simular_entradas(foto):
    print(f"foto de pessoas: {foto}")

    pessoas = {
        "foto": foto,
        "alunos_cadastrados": None
    }

    return pessoas


def reconhecer_alunos(configuracao, pessoas):
    foto_pessoas = reconhecedor.load_image_file(pessoas["foto"])
    caracteristicas_dos_pessoas = reconhecedor.face_encodings(
        foto_pessoas)

    alunos_cadastrados = []
    for aluno in configuracao["alunos_cadastrados"]:
        fotos = aluno["fotos"]
        total_de_reconhecimentos = 0

        for foto in fotos:
            foto = reconhecedor.load_image_file(foto)
            caracteristicas = reconhecedor.face_encodings(foto)[0]

            reconhecimentos = reconhecedor.compare_faces(
                caracteristicas_dos_pessoas, caracteristicas)
            if True in reconhecimentos:
                total_de_reconhecimentos += 1

        if total_de_reconhecimentos/len(fotos) >= 0.6:
            alunos_cadastrados.append(aluno)

    return (len(alunos_cadastrados) > 0), alunos_cadastrados


def imprimir_dados_do_aluno(aluno):
    print(colored.fg('black'), colored.bg(
        'yellow'), f"aluno reconhecido: ", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"nome: {aluno['nome']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"idade: {aluno['idade']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"endereço: {aluno['endereco']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"matricula: {aluno['matricula']}", colored.attr('reset'))
    print(colored.fg('black'), colored.bg(
        'yellow'), f"turma: {aluno['turma']}", colored.attr('reset'))


def identificar_cadastro_paae(alunos_reconhecidos):
    total_de_alunos_cadastrados_paae = 0

    for id_reconhecimento, aluno in list(alunos_reconhecidos.items()):
        if not aluno.get("bolsa_paae_verificada", False):
            possui_bolsa_paae = aluno.get("bolsa_paae", "Não")
            if possui_bolsa_paae == "Sim":
                alunos_reconhecidos[id_reconhecimento]["bolsa_paae_verificada"] = True

                total_de_alunos_cadastrados_paae += 1

    return total_de_alunos_cadastrados_paae


def liberar_alunos(alunos_reconhecidos, probabilidade_de_liberacao):
    total_de_alunos_liberados = 0

    for id_reconhecimento, aluno in list(alunos_reconhecidos.items()):
        if aluno["bolsa_paae_verificada"]:
            aluno_liberado = (random.randint(
                1, 100)) <= probabilidade_de_liberacao
            if aluno_liberado:
                alunos_reconhecidos.pop(id_reconhecimento)
                
                total_de_alunos_liberados += 1
    
    return total_de_alunos_liberados

def simular_alerta_pessoas_nao_cadastradas(configuracao):
    total_de_pessoas_nao_cadastradas = 0

    for pessoa in configuracao["pessoas_nao_cadastradas"]:
        matricula_pessoa = pessoa.get("matricula")
        if matricula_pessoa not in [aluno["matricula"] for aluno in configuracao["alunos_cadastrados"]]:
            print(colored.fg('black'), colored.bg('red'),
                  f"Nome: {pessoa['nome']}", colored.attr('reset'))

            total_de_pessoas_nao_cadastradas += 1

    return total_de_pessoas_nao_cadastradas

