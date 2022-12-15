import sqlite3
conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()

#Faz uma consulta no banco e retorna uma lista com todos os dados de aluno
def carregarDadosAlunos():
    global conn
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM alunos')
    listaAlunos = cursor.fetchall()

    cursor.close()
    return listaAlunos

#Faz uma consulta no banco e retorna uma lista com todos os dados de professores
def carregarDadosProfessores():
    global conn
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM professores')
    listaProfessores = cursor.fetchall()

    cursor.close()
    return listaProfessores

#Faz uma consulta no banco e retorna uma lista com todos os dados de disciplinas
def carregarDadosDisciplinas():
    global conn
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM disciplinas')
    listaDisciplinas = cursor.fetchall()

    cursor.close()
    return listaDisciplinas

#Faz uma consulta no banco e retorna uma lista com todos os dados de notas
def carregarDadosNotas():
    global conn
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM notas')
    listaNotas = cursor.fetchall()
    
    cursor.close()
    return listaNotas

#Funcao responsável por salvar todos os dados contidos nos dicionários dentro do banco de dado
def salvarDadosNoBanco(alunos,disciplinas,professores,notas):
    global conn
    cursor = conn.cursor()
    
    for key,value in alunos.items():
        consulta = 'INSERT OR IGNORE INTO alunos (matricula_aluno, nome_aluno, data_nascimento) VALUES (?,?,?)'
        cursor.execute(consulta,(key,value['nome'],value['data_nascimento']))
        conn.commit()
    for key,value in professores.items():
        consulta = 'INSERT OR IGNORE INTO professores (matricula_professor, nome_professor, data_nascimento) VALUES (?,?,?)'
        cursor.execute(consulta,(key,value['nome'],value['data_nascimento']))
        conn.commit()
    for key,value in disciplinas.items():
        consulta = 'INSERT OR IGNORE INTO disciplinas (codigo_disciplina, nome_disciplina, matricula_professor) VALUES (?,?,?)'
        cursor.execute(consulta,(key,value['nome_disciplina'],value['matricula_professor']))
        conn.commit()
    for key,value in notas.items():
        for nota in value:
            consulta = "SELECT matricula_aluno, codigo_disciplina FROM notas"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            conn.commit()
            for r in resultado:
                if nota['codigo_disciplina'] in r and nota['matricula_aluno'] in r:
                    print('nota para o aluno na disciplina já cadastrada!')
                    return
            consulta2 = 'INSERT OR IGNORE INTO notas (codigo_disciplina, matricula_aluno, nota_01, nota_02, media) VALUES (?,?,?,?,?)'
            cursor.execute(consulta2,(nota['codigo_disciplina'],nota['matricula_aluno'],nota['nota_01'],nota['nota_02'],nota['media']))
            conn.commit()
    cursor.close()