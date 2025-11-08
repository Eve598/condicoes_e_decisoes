class aluno:
    nome = "" 
    nota = 0

    def mostrar(self):
        if self.nota <= 5:
            print(self.nome, "foi reprovado/a/e/x")

        else:
            print(self.nome, "foi aprovado/a/e/x")

a1 = aluno()
a1.nome = "diego"
a1.nota = -9

a1.mostrar()


a2 = aluno()
a2.nome = "Déborah"
a2.nota = -100

a2.mostrar()

a3 = aluno()
a3.nome = "rodrigo"
a3.nota = -0

a3.mostrar()

a4 = aluno()
a4.nome = "thayana"
a4.nota = 9

a4.mostrar()

a5 = aluno()
a5.nome = "gabby"
a5.nota = 8

a5.mostrar()

a6 = aluno()
a6.nome = "enzo"
a6.nota = 10

a6.mostrar()