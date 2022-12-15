from menu import menu
from time import sleep
from Escola import *



'''Limpa tela do terminal'''


def limpartela():
    return print('\n' * 100)


'''Controla o programa baseado na escolha da entrada'''


# Parâmetros: escola(Instância de Escola), entrada(valor escolhido pelo usuário no Menu)
def controlador(escola, entrada):
    limpartela()
    match entrada:
        case 1:
            print('\n******* Cadastro de Professores ******\n')
            nome_professor = input('Informe o Nome do Professor(A): ')
            matricula_professor = str(input(f'Matricula do Professor({nome_professor}): '))
            data_nascimento = str(input(f'Informe a data de nascimento do Professor({nome_professor}): '))
            escola.cadastrar_de_professores(nome_professor, matricula_professor, data_nascimento)
            sleep(2)

        case 2:
            print('\n******* Cadastro de Alunos ******\n')
            nome_aluno = input('Informe o Nome do Aluno(A): ')
            matricula_aluno = str(input(f'Matricula do Aluno({nome_aluno}): '))
            data_nascimento = str(input(f'Informe a data de nascimento do Aluno({nome_aluno}): '))
            escola.cadastrar_alunos(nome_aluno, matricula_aluno, data_nascimento)
            sleep(2)

        case 3:
            print('\n******* Cadastro de Disciplinas ******\n')
            codigo_disciplina = str(input(f'Código da disciplina: '))
            nome_disciplina = input(f'Informe o nome da disciplina({codigo_disciplina}): ')
            matricula_professor = str(input(f'Matricula do Professor(a) da disciplina: '))
            escola.cadastrar_de_diciplinas(codigo_disciplina, nome_disciplina, matricula_professor)
            sleep(2)

        case 4:
            print('\n******* Cadastro de Notas ******\n')
            codigo_disciplina = str(input(f'Código da disciplina: '))
            matricula_aluno = str(input(f'Matricula do aluno(a): '))
            nota_01 = float(input(f'Nota 1 do Aluno({matricula_aluno}): '))
            nota_02 = float(input(f'Nota 2 do aluno({matricula_aluno}): '))
            escola.cadastrar_notas(codigo_disciplina, matricula_aluno, nota_01, nota_02)
            sleep(2)

        case 5:
            print('\n******* Relatório de Notas ******\n')
            codigo_disciplina = str(input(f'Código da disciplina: '))
            escola.relatorio_notas(codigo_disciplina)

        case 6:
            escola.salvarDados()
            limpartela()
            print('.salvando')
            sleep(1)
            limpartela()
            print('..salvando')
            sleep(1)
            limpartela()
            print('...salvando')
            sleep(1)
            limpartela()
            print('Salvo com exito!')
            sleep(1)
            print('Saindo! \n')
    return


def main():
    # Cria uma instacia de Cinema
    escola = Escola()

    # Armazena a opção do Menu. Condição inicial: 0(nulo)
    entrada = 0

    # Função responsável por "limpar" a tela do terminal
    limpartela()

    # While:
    # Condição de parada -> entrada == 9
    while entrada != 6:
        # Funcao responsável por imprimir o Menu para o usuário
        menu()
        entrada = int(input('>'))

        # Controlador do programa.
        # Responsável por controlar as funções baseado no valor da entrada
        controlador(escola, entrada)


if __name__ == '__main__':
    main() 