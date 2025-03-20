# Função para cadastrar alunos e registrar notas
def cadastrar_alunos():
    alunos = []
    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
        if nome.lower() == 'fim':
            break
        
        notas = {}
        for materia in ['Matemática', 'Português', 'Ciências', 'História', 'Geografia']:
            notas_materia = []
            for bimestre in range(1, 5):
                nota = float(input(f"Digite a nota de {materia} no {bimestre}º bimestre: "))
                notas_materia.append(nota)
            notas[materia] = notas_materia
        alunos.append({'nome': nome, 'notas': notas})
    return alunos

# Função para calcular a média das notas por matéria
def calcular_media(notas):
    medias = {}
    for materia, notas_materia in notas.items():
        medias[materia] = sum(notas_materia) / len(notas_materia)
    return medias

# Função para exibir os resultados e salvar em um arquivo
def exibir_resultados(alunos):
    with open("relatorio_de_notas.txt", "w") as arquivo:
        for aluno in alunos:
            nome = aluno['nome']
            notas = aluno['notas']
            medias = calcular_media(notas)
            
            arquivo.write(f"Aluno: {nome}\n")
            print(f"Aluno: {nome}")
            
            for materia, media in medias.items():
                arquivo.write(f"Média de {materia}: {media:.2f}\n")
                print(f"Média de {materia}: {media:.2f}")
            
            arquivo.write("-" * 50 + "\n")
            print("-" * 50)

# Função principal para executar o programa
def main():
    alunos = cadastrar_alunos()
    exibir_resultados(alunos)

# Executar o programa
if __name__ == "__main__":
    main()
