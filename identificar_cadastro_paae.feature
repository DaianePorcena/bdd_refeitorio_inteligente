Feature: identificando se existe algum aluno cadastrado no paae

    Scenario: um aluno reconhecido precisa verificar se está cadastrado no paae
        Given o ambiente de desenvolvimento esteja preparado corretamente
        When a foto /home/daiane/Área de Trabalho/Faculdade/IHM/refeitorio_inteligente/bdd_refeitorio_inteligente/faces/alunos2.jpg de pessoas for capturada
        Then pelo menos, um(a) aluno deve ser reconhecido
        when um cadastro for identificado
        Then pelo menos, um(a) terá o acesso ao refeitório

