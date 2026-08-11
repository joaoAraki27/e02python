livro = {
    "título": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899,
}

print(livro["título"])
print(livro["ano"])

livro["ano"] = 1990
livro["editora"] = "Garnier"

print(livro)

# .items() entrega os dois de uma vez: a chave e o valor
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

if "ano" in livro:
    print("tem ano")

if "paginas" not in livro:
    print("nao tem paginas")

acervo = [
    {"titulo": "Dom Casmurro", "autor":"Machado de Assis","ano":1899},
    {"titulo": "Vidas Secas", "autor":"Graciliano Ramos","ano":1899},
    {"titulo": "Grande Sertao", "autor":"Guimaraes Rosa","ano":1899},
]

print("livros no acervo:", len(acervo))

for livro in acervo:
    print(f'{livro["titulo"]} ({livro["ano"]}) {livro["autor"]}')

procurando = input("Titulo: ")
encontrado = None

for livro in acervo:
    if livro["titulo"] == procurando:
        encontrado = livro
        break

if encontrado:
    print(f'Autor: {encontrado["autor"]}')
else:
    print("Nao esta no acervo")