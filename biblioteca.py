acervo = []

while True:
    print("""
    1 — Cadastrar
    2 — Consultar
    3 — Listar
    0 — Sair
    """)

    resposta = input("Escolha uma opção: ")

    if resposta == "1":
        print("Para cadastrar um livro, dê as informações abaixo:")

        titulo = input("Título da obra: ")
        autor = input("Autor da obra: ")
        ano = int(input("Ano da obra: "))

        acervo.append({"titulo": titulo, "autor": autor, "ano": ano})

        print("Livros no acervo:", len(acervo))
        print("Livro cadastrado com sucesso!")

    elif resposta == "2":
        titulo = input("Que livro você quer consultar? Dê o título: ")

        encontrado = False

        for livro in acervo:
            if livro["titulo"] == titulo:
                print(f'Autor: {livro["autor"]}')
                print(f'Ano: {livro["ano"]}')
                encontrado = True
                break

        if not encontrado:
            print("Não está no acervo")

    elif resposta == "3":
        if len(acervo) == 0:
            print("O acervo está vazio.")
        else:
            for livro in acervo:
                print(f'{livro["titulo"]} ({livro["ano"]}) - {livro["autor"]}')

            print(f"Total: {len(acervo)} livros.")

    elif resposta == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")