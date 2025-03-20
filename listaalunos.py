def listar_alunos(alunos):
    print("\nLista de Alunos Cadastrados:")
    for nome in alunos:
        print(f"- {nome}")

# Função principal modificada para incluir a lista de alunos
def main():
    alunos = cadastrar_alunos()
    listar_alunos(alunos)  # Lista de alunos cadastrados
    medias = calcular_media(alunos)
    exibir_desempenho_por_materia(alunos, medias)
    exibir_desempenho_geral(medias)
    exibir_maior_menor_media(alunos, medias)

# Executar o programa
if __name__ == "__main__":
    main()
