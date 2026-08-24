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

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        if valor < 1450 or valor > 2026:
            raise ValueError(f"Ano invalido: {valor}")
        self._ano = valor


class Usuario:
    def __init__(self, nome, matricula, limite ):
        if not nome:
            raise ValueError("Nome e obrigatorio")
        self.nome = nome
        self.matricula = matricula
        self.limite = 3

        if self.limite == 0:
            print("atingiu limite")
            return False

    def __str__(self):
        return f"self.limite = limite + 1 {self.nome} ({self.matricula})" 
    
    


class emprestimo:
    def __init__(self, livro, usuario, data):
        self.livro = livro
        self.usuario = usuario
        self.data = data
        self.devolvido = False

    def devolver(self):
        if self.devolvido:
            raise ValueError("Este emprestimo ja foi devolvido")
        self.devolvido = True

    def __str__(self):
        estado = "devolvido" if self.devolvido else "em aberto"
        return f"{self.livro.título} -> {self.usuario.nome} ({estado})"

    

if __name__ =="__main__":

    acervo = [
    Livro("Dom Casmurro", "Machado de Assis", 1899),
    Livro("O Cortiço", "Aluísio Azevedo", 1890),
    Livro("Os Sertões", "Euclides da Cunha", 1902),

    ]

    for livro in acervo:
        print(livro.descricao(), "-", livro.idade(), "anos")

# Livro("Teste", "Alguemm", 3000)
    

# for livro in acervo:
#     print(livro.título, "-", livro.ano)

livro = Livro("Dom Casmurro", "Machado de Assis", 1899)


print(livro.título)
print(livro.ano)

ana = Usuario("Ana Souza", "2026001",3)
emp = emprestimo(livro, ana, "20/08/2026")

print(emp)
print(emp.livro.autor)
print(emp.usuario.matricula)

emp.devolver()
print(emp)
emp.devolver()