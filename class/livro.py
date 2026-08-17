class Livro:

    def __init__(self, título, autor, ano):

        if not título:
            raise ValueError("Título e obrigatório")
        if ano < 1450 or ano > 2026:
            raise ValueError(f"Ano invalido: {ano}")

        
        self.título = título
        self.autor = autor
        self.ano = ano

        def descricao(self):
            return f"{self.título} - {self.autor} ({self.ano})"

        def idade(self):
            return 2026 - self.ano

        def e_classico(self):
            if self.ano > 100:
                return True
            else:
                return False
        
acervo = [
    Livro("Dom Casmurro", "Machado de Assis", 1899),
    Livro("O Cortiço", "Aluísio Azevedo", 1890),
    Livro("Os Sertões", "Euclides da Cunha", 1902),

]

if __name__ =="__main__":

    acervo = [
        Livro("Dom Casmurro", "Machado de Assis", 1899),
        Livro("Iracema", "Jose de Alencar", 1865),
    ]

    for livro in acervo:
        print(livro.descricao(), "-", livro.idade(), "anos")

        Livro("Teste", "Alguemm", 3000)



    

for livro in acervo:
    print(livro.título, "-", livro.ano)

livro =Livro("Dom Casmurro", "Machado de Assis", 1899)


print(livro.título)
print(livro.ano)