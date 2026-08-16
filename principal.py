from acervo import cadastrar, buscar, listar


livros = []

while True:
    print("\n--- ACERVO DE LIVROS ---")
    print("1 - Cadastrar livro")
    print("2 - Buscar livro")
    print("3 - Listar livros")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))

        cadastrar(livros, titulo, autor, ano)
        print("Livro cadastrado com sucesso.")

    elif opcao == "2":
        titulo = input("Título para buscar: ")
        achado = buscar(livros, titulo)

        if achado:
            print(f'Título: {achado["titulo"]}')
            print(f'Autor: {achado["autor"]}')
            print(f'Ano: {achado["ano"]}')
        else:
            print("Não está no acervo.")

    elif opcao == "3":
        resultado = listar(livros)

        if not resultado:
            print("O acervo está vazio.")
        else:
            print("\n--- LIVROS CADASTRADOS ---")

            for livro in resultado:
                print(
                    f'{livro["titulo"]} - '
                    f'{livro["autor"]} - '
                    f'{livro["ano"]}'
                )

            print(f"Total: {len(resultado)} livro(s).")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
