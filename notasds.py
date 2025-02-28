# Função para cadastrar alunos e suas notas
def cadastrar_alunos():
    alunos = {}
    num_alunos = int(input("Digite o número de alunos: "))
    
    for i in range(num_alunos):
        nome = input(f"Digite o nome do {i+1}º aluno: ")
        num_materias = int(input(f"Quantas matérias {nome} está cursando? "))
        
        # Criar um dicionário para armazenar as notas de cada aluno
        aluno = {
            'nome': nome,
            'notas': {}
        }
        
        # Cadastrar notas para cada matéria
        for materia in range(1, num_materias + 1):
            print(f"\nCadastro de notas para a {materia}ª matéria de {nome}:")
            notas_materia = []
            for bimestre in range(1, 5):  # 4 bimestres
                while True:
                    try:
                        nota = float(input(f"Nota do {bimestre}º bimestre: "))
                        if 0 <= nota <= 10:
                            notas_materia.append(nota)
                            break
                        else:
                            print("A nota deve estar entre 0 e 10. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida! Digite um número válido.")
            
            aluno['notas'][f'Matéria {materia}'] = notas_materia
        
        alunos[nome] = aluno
    
    return alunos

# Função para calcular a média de cada matéria para cada aluno
def calcular_media(alunos):
    medias = {}
    
    for aluno in alunos.values():
        medias_aluno = {}
        for materia, notas in aluno['notas'].items():
            media_materia = sum(notas) / len(notas)
            medias_aluno[materia] = media_materia
        medias[aluno['nome']] = medias_aluno
    
    return medias

# Função para exibir o desempenho de cada aluno por matéria
def exibir_desempenho_por_materia(alunos, medias):
    print("\nDesempenho dos alunos por matéria:")
    for nome, aluno in alunos.items():
        print(f"\nAluno: {nome}")
        for materia, media in medias[nome].items():
            print(f"{materia} - Média: {media:.2f}")
        print("-" * 40)

# Função para exibir o desempenho geral de todas as matérias
def exibir_desempenho_geral(medias):
    print("\nDesempenho Geral por Matéria:")
    
    num_materias = len(medias[next(iter(medias))])  # Pega o número de matérias de qualquer aluno
    for i in range(1, num_materias + 1):
        materia = f"Matéria {i}"
        medias_materia = [medias[aluno][materia] for aluno in medias]
        media_geral = sum(medias_materia) / len(medias_materia)
        maior_media = max(medias_materia)
        menor_media = min(medias_materia)
        print(f"\n{materia}:")
        print(f"Média Geral: {media_geral:.2f}")
        print(f"Maior Média: {maior_media:.2f}")
        print(f"Menor Média: {menor_media:.2f}")
        print("-" * 40)

# Função para exibir a maior e menor média de um aluno
def exibir_maior_menor_media(alunos, medias):
    print("\nMaior e Menor Média de Cada Aluno:")
    for nome, aluno in alunos.items():
        media_geral = sum(medias[nome].values()) / len(medias[nome])
        maior_media = max(medias[nome].values())
        menor_media = min(medias[nome].values())
        print(f"\nAluno: {nome}")
        print(f"Média Geral: {media_geral:.2f}")
        print(f"Maior Média: {maior_media:.2f}")
        print(f"Menor Média: {menor_media:.2f}")
        print("-" * 40)

# Função principal que organiza a execução
def main():
    alunos = cadastrar_alunos()
    medias = calcular_media(alunos)
    exibir_desempenho_por_materia(alunos, medias)
    exibir_desempenho_geral(medias)
    exibir_maior_menor_media(alunos, medias)

# Executar o programa
if __name__ == "__main__":
    main()