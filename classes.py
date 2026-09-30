class Livro:
    def __init__(self, titulo, autor, num_paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.genero = genero

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

meu_livro = Livro(titulo='Verity', autor='Collen Hoover', num_paginas=300, genero='Thriller')

print('Titulo do livro: ', meu_livro.get_titulo())

meu_livro.set_titulo(titulo="Assim que acaba")

print("Novo Título do livro: ", meu_livro.get_titulo())