class Usuario:
    def __init__(self, nome, matricula):
        if not nome:
            raise ValueError("Nome e obrigatorio")
        self.nome = nome
        self.matricula = matricula
        self.limite = 3

        # if self.limite == 0:
        #     print("atingiu limite")
        #     return False

    def __str__(self):
        return f"self.limite = limite + 1 {self.nome} ({self.matricula})" 