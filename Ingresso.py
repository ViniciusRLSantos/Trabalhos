class CriarIngresso:
    inteira = 24
    meia = 12
    sessao_selecionada = "Nenhuma"
    total_final = 0
    def __init__(self, qntdinteira, qntdmeia, sessao=None):
        self.qntdinteira = qntdinteira
        self.qntdmeia = qntdmeia
        if sessao is None:
            self.sessao = []
        else:
            self.sessao = sessao

    def adicionarSessao(self, dia, horario):
        self.dia = dia
        self.horario = horario
        ses = dia + " - " + horario
        if (ses not in self.sessao):
            self.sessao.append(ses)

    def removerSessao(self, dia, horario):
        self.dia = dia
        self.horario = horario
        ses = dia + " - " + horario
        if (ses in self.sessao):
            self.sessao.remove(ses)

    # Essa função vai listar todas as sessões disponíveis
    def listarSessoes(self):
        for i in self.sessao:
            index = self.sessao.index(i)
            print("[" + str(index+1) + "] " + i)
