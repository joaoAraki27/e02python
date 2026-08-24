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

