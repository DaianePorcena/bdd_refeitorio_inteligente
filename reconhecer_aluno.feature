Feature: reconhecimento de alunos

    Scenario: um aluno deve ser reconhecido através de uma foto de pessoas entrando no ambiente
        Given o ambiente de reconhecimento esteja preparado corretamente
        When a foto /home/daiane/Área de Trabalho/Faculdade/IHM/refeitorio_inteligente/bdd_refeitorio_inteligente/faces/alunos1.jpg de pessoas for capturada
        Then pelo menos, um(a) aluno deve ser reconhecido
    
    Scenario: não deve reconhecer alunos quando eles não estão entre as pessoas no ambiente
        Given o ambiente de reconhecimento esteja preparado corretamente
        When a foto faces/pessoas.jpg de pessoas for capturada
        Then nenhum(a) aluno deve ser reconhecido

    Scenario Outline: reconhecer alunos de varias fotos diferentes
        Given o ambiente de reconhecimento esteja preparado corretamente
        When a foto <foto_capturada> de pessoas for capturada
        Then <total_de_reconhecimentos> alunos devem ser reconhecidos

        Examples:
            | foto_capturada                                                                | total_de_reconhecimentos |
                |  /home/daiane/Área de Trabalho/Faculdade/IHM/refeitorio_inteligente/bdd_refeitorio_inteligente/faces/alunos1.jpg | 2                        |
                |  /home/daiane/Área de Trabalho/Faculdade/IHM/refeitorio_inteligente/bdd_refeitorio_inteligente/faces/alunos2.jpg | 2                        |
                |  /home/daiane/Área de Trabalho/Faculdade/IHM/refeitorio_inteligente/bdd_refeitorio_inteligente/faces/alunos3.jpg | 1                        |
                |  /home/daiane/Área de Trabalho/Faculdade/IHM/refeitorio_inteligente/bdd_refeitorio_inteligente/faces/alunos4.jpg | 1                        |
                |  /home/daiane/Área de Trabalho/Faculdade/IHM/refeitorio_inteligente/bdd_refeitorio_inteligente/faces/pessoas.jpg | 0                        |