Feature: verificando se existem alunos para serem liberados

    Scenario: um aluno que entrou no refeitorio deve ser liberado
        Given o ambiente de desenvolvimento esteja preparado corretamente
        When a foto /home/daiane/Área de Trabalho/Faculdade/IHM/refeitorio_inteligente/bdd_refeitorio_inteligente/faces/alunos2.jpg de pessoas for capturada
        Then pelo menos, um(a) aluno deve ser reconhecido
        When a probabilidade de liberacao for 100 porcento
        Then pelo menos, um(a) aluno deve ser liberado