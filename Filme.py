class CriarFilme:
    lista_de_filmes = []
    filme_selecionado = "Nenhum"

    def __init__(self, nomefilme, descricao, nomeautor, genero, duracao):
        self.nomefilme = nomefilme
        self.descricao = descricao
        self.nomeautor = nomeautor
        self.genero = genero
        self.duracao = duracao

        CriarFilme.lista_de_filmes.append(self.nomefilme)

    # Essa função irá mostrar as informações do filme
    def mostrarInfo(self):
        print("Filme: "+self.nomefilme)
        print("Descrição: "+self.descricao)
        print("Autor: "+self.nomeautor)
        print("Gênero: "+self.genero)
        print("Duração: "+str(self.duracao) + "min")


def mostrarFilmes():
    for filme in CriarFilme.lista_de_filmes:
        index = CriarFilme.lista_de_filmes.index(filme) + 1
        print("[{}] - {}".format(str(index), filme))
