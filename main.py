from Filme import CriarFilme, mostrarFilmes
from Ingresso import CriarIngresso

filme1 = CriarFilme("Desventuras de um Careca Bombado",
                  "Calvino Clementino teve uma vida bem infortuna. Além de ser calvo de nascença, ter 1.68 de altura e canhoto, ele sempre foi muito azarado e sempre\n"
                  "esteve em situações de alto perigo, mas sempre conseguiu sobressair e manteve seu bom coração. Após tantos eventos horríveis, ele acabou se adaptando\n"
                  "aos perigos e acabou ficando bombado e extremamente forte. Agora, o novo herói careca terá de derrotar Richard the Chad, um homem que sempre teve tudo\n"
                  "que queria sem esforço que agora quer dominar o mundo.",
                  "Vini", "Ação & Comédia", 120)

filme2 = CriarFilme("Sonhos Longos", "descrição", "Junji Ito", "Terror psicológico", 95)

filme3 = CriarFilme("Feitiço do Tempo",
                    "Phil, um arrogante meteorologista de um canal de televisão, fica preso em uma espécie de túnel do tempo, condenado a reviver indefinidamente o mesmo dia\n"
                    "até que mude suas atitudes.",
                    "Harold Ramis", "Comédia Dramática & Fantasia", 101)

ingresso = CriarIngresso(0, 0)
ingresso.adicionarSessao("16/11/2022", "22:40")
ingresso.adicionarSessao("10/12/2022", "19:50")
ingresso.adicionarSessao("23/12/2022", "20:30")
ingresso.adicionarSessao("5/01/2023", "21:50")
ingresso.adicionarSessao("08/01/2023", "00:30")


lista_objFilmes = [filme1, filme2, filme3]


def selecionarFilme():
    print("Filmes no ar:")
    mostrarFilmes()
    sel_filme = int(input("Selecione um filme: "))

    if sel_filme <= len(CriarFilme.lista_de_filmes)+1:
        print("\nVocê selecionou o filme: {}".format(CriarFilme.lista_de_filmes[sel_filme-1]))
        print("\nInformações:")
        lista_objFilmes[sel_filme-1].mostrarInfo()

        confirmar = input("Confirmar seleção de filme? [Y/N] (sim e não respectivamente): ")
        if confirmar[0] == "Y" or confirmar[0] == "S":
            CriarFilme.filme_selecionado = lista_objFilmes[sel_filme-1].nomefilme
        else:
            selecionarFilme()
    else:
        print("\n\n\n*****SELECIONE UM FILME VÁLIDO*****\n\n\n")
        selecionarFilme()


def selecionarIngresso():
    print("Compra do Ingresso\nINTEIRA - R$24,00\nMEIA - R$12,00\n\n")
    ing_inteiro = int(input("Quantidade de ingressos [VALOR INTEIRO]: "))
    ing_meia = int(input("Quantidade de ingressos [MEIA ENTRADA]: "))
    total = ing_inteiro*24 + ing_meia*12

    print("Sessões disponíveis:\n")
    ingresso.listarSessoes()
    sel_sessao = int(input("Selecione uma sessão: "))
    if sel_sessao <= len(ingresso.sessao):
        print("\nVocê selecionou a sessão de {} no valor de R${},00".format(ingresso.sessao[sel_sessao-1], total))

        confirmar = input("Confirmar? [Y/N] (sim e não respectivamente): ")
        if confirmar[0] == "Y" or confirmar[0] == "S" or confirmar[0] == "y" or confirmar[0] == "s":
            CriarIngresso.sessao_selecionada = ingresso.sessao[sel_sessao - 1]
            CriarIngresso.total_final = total
        else:
            selecionarIngresso()


selecionarFilme()
selecionarIngresso()
print("O(s) ingresso(s) para o filme {} na sessão {} no valor de R${},00 foi realizada com sucesso!\nBom filme!".format(CriarFilme.filme_selecionado, CriarIngresso.sessao_selecionada, CriarIngresso.total_final))