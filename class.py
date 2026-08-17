class Pessoa:
    def __init__(self, nome, peso,altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imc(self): #método
        return(self.peso / (self.altura * self.altura))

    def ver_imc(self):
        return...

ana = Pessoa("Ana", 80, 1.8)

print(ana.nome, "- ", ana.peso)
print(ana.nome, " - ", round(ana.imc()))