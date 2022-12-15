import dados as bd

#Variveis Globais
professores = {}
alunos = {}
disciplinas = {}
notas = {}
dados_notas = []
lista_aux = []

#Funcao que carrega os dados do banco para os respectivos dicionários
def iniciaDicionarios():
    global professores, alunos,disciplinas,notas
    
    #Loop para carregar os dados do banco para o dicionario de professores
    for p in bd.carregarDadosProfessores():
        professores[p[0]] = {'nome': p[1], 'data_nascimento': p[2]}
        
    #Loop para carregar os dados do banco para o dicionario de alunos
    for a in bd.carregarDadosAlunos():
        alunos[a[0]] = {'nome': a[1], 'data_nascimento': a[2]}
        
    #Loop para carregar os dados do banco para o dicionario de disciplinas
    for d in bd.carregarDadosDisciplinas():
        disciplinas[d[0]] = {'nome_disciplina':d[1], 'matricula_professor': d[2]}
     
    #Loop para carregar os dados do banco para o dicionario de notas    
    for n in bd.carregarDadosNotas():
        lista_aux = []
        if n[1] in alunos:
            if n[0] in disciplinas:
                print(n[1])
                if n[0] not in notas:
                    lista_aux.append({'matricula_aluno': n[1], 'codigo_disciplina': n[0],'nota_01': n[2], 'nota_02': n[3], 'media': n[4]})
                    notas.update({n[1]: lista_aux})
                    print(notas)
                else:    
                    for nota in notas[n[1]]:
                        lista_aux.append(nota)
                    lista_aux.append({'matricula_aluno': n[1], 'codigo_disciplina': n[0],'nota_01': n[2], 'nota_02': n[3], 'media': n[4]})
                    notas.update({n[1]: lista_aux})
        
#Classe Escola
class Escola:
    def __init__(self):
        global alunos, professores
        iniciaDicionarios()
        print('👍👍👍')
        print('Alunos:',alunos,'\nProfessores:', professores,'\nDisciplinas:', disciplinas,'\nNotas:', notas)

    #Funcao que cadastra professores
    def cadastrar_de_professores(self, nome, matricula, data_nascimento):
        global professores
        if matricula not in professores:
            professores[matricula] = {'nome': nome, 'data_nascimento': data_nascimento}
            return print('Professor(a) cadastrado!')
        return print('Professor(a) já cadastrado. ❌')
    
    #Funcao que cadastra alunos
    def cadastrar_alunos(self, nome, matricula, data_nascimento):
        global alunos
        if matricula not in alunos:
            alunos[matricula] = {'nome': nome, 'data_nascimento': data_nascimento}
            return print('Aluno(a) cadastrado!')
        return print('Aluno(a) já cadastrado. ❌')

    #Funcao que cadastra disciplinas
    def cadastrar_de_diciplinas(self, codigo_disciplina, nome_disciplina, matricula_professor):
        global professores, disciplinas
        if matricula_professor in professores:
            if codigo_disciplina not in disciplinas:
                disciplinas[codigo_disciplina] = {'nome_disciplina': nome_disciplina, 'matricula_professor': matricula_professor}
                return print('Disciplina cadastrada!')
            return print('Disciplina já cadastrada! ❌')
        print('Matrícula do professor não cadastrada! ❌')
        return

    #Funcao que cadastra notas
    def cadastrar_notas(self, codigo_disciplina, matricula_aluno, nota_01, nota_02):
        global alunos, disciplinas, notas, dados_notas, lista_aux
        if matricula_aluno in alunos.keys():
            lista_aux = []
            if codigo_disciplina in disciplinas:
                media = round(((nota_01 + nota_02) / 2), 2)
                if matricula_aluno not in notas.keys():
                    lista_aux.append({'matricula_aluno': matricula_aluno, 'codigo_disciplina': codigo_disciplina,
                                      'nota_01': nota_01, 'nota_02': nota_02, 'media': media})
                    notas.update({matricula_aluno: lista_aux})
                    return print('Nota cadastrada!')
                for nota in notas[matricula_aluno]:
                    lista_aux.append(nota)
                lista_aux.append(
                    {'matricula_aluno': matricula_aluno, 'codigo_disciplina': codigo_disciplina, 'nota_01': nota_01,
                     'nota_02': nota_02, 'media': media})
                notas.update({matricula_aluno: lista_aux})
                print('Nota cadastrada!')
            return print('Disciplina não cadastrada! ❌')
        return print('Matrícula não cadastrada. ❌')

    #Funcao que cria o relatório notas
    def relatorio_notas(self, codigo_disciplina):
        global disciplinas, notas, professores, alunos
        if codigo_disciplina in disciplinas: 
            print(f"Disciplina: {disciplinas[codigo_disciplina]['nome_disciplina']}\nProfessor: {disciplinas[codigo_disciplina]['matricula_professor']}")
            for aluno in alunos.keys():
                if aluno in notas.keys():
                    for i in notas[aluno]:
                        if i['codigo_disciplina'] == codigo_disciplina:
                            print(f"Matrícula: {aluno} - Nota 1: {i['nota_01']} Nota 2: {i['nota_02']} Média : {i['media']}")
            return
        return print('Disciplina não cadastrada! ❌')
    
    #Funcao responsável por enviar os dicionários 
    def salvarDados(self):
        global alunos,disciplinas,professores, notas
        bd.salvarDadosNoBanco(alunos,disciplinas,professores, notas)