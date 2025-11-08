class Pessoa:
    nome = ""
    idade = 0

    def verificar_maioridade(self):
        if self.idade >= 18:
            print(f"{self.nome} é maior de idade")
        else:
            print(f"{self.nome} é menor de idade")


p1 = Pessoa()
p1.nome = "Evelyn"
p1.idade = 16
print("Nome:", p1.nome, "Idade:", p1.idade)
p1.verificar_maioridade()

p2 = Pessoa()
p2.nome = "Déborah"
p2.idade = 21
print("Nome:", p2.nome, "Idade:", p2.idade)
p2.verificar_maioridade()

p3 = Pessoa()
p3.nome = "Nhooo"
p3.idade = 17
print("Nome:", p3.nome, "Idade:", p3.idade)
p3.verificar_maioridade()

p4 = Pessoa()
p4.nome = "Nheee"
p4.idade = 13
print("Nome:", p4.nome, "Idade:", p4.idade)
p4.verificar_maioridade()

p5 = Pessoa()
p5.nome = "Nhaaa"
p5.idade = 22
print("Nome:", p5.nome, "Idade:", p5.idade)
p5.verificar_maioridade()

p6 = Pessoa()
p6.nome = "Cátia"
p6.idade = 45
print("Nome:", p6.nome, "Idade:", p6.idade)
p6.verificar_maioridade()

p7 = Pessoa()
p7.nome = "Gabby"
p7.idade = 17
print("Nome:", p7.nome, "Idade:", p7.idade)
p7.verificar_maioridade()

p8 = Pessoa()
p8.nome = "Thay"
p8.idade = 17
print("Nome:", p8.nome, "Idade:", p8.idade)
p8.verificar_maioridade()

p9 = Pessoa()
p9.nome = "Enzo"
p9.idade = 17
print("Nome:", p9.nome, "Idade:", p9.idade)
p9.verificar_maioridade()

p10 = Pessoa()
p10.nome = "Felipe"
p10.idade = 28
print("Nome:", p10.nome, "Idade:", p10.idade)
p10.verificar_maioridade()
