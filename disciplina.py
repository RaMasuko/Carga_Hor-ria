class Disciplina:
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria

    def exibir_info(self):
        print(f"Diciplina: {self.nome} - Carga: {self.carga_horaria} horas")