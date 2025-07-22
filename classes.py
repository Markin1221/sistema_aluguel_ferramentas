class Ferramentas:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    #
    # def calcular_diaria(self, dias):
    #     return self.preco * dias
    #
    # def calcular_semanal(self, semana):
    #     return (self.preco * semana) * 0.95
    #
    # def calcular_mensal(self, meses):
    #     return (self.preco * meses) * 0.9

class Aluguel:
    def __init__(self, ferramenta, dias, entrega=False, retirada=False, atraso=0,
                 danificado=False, sujo=False, cancelado=False, cancelamento_24h=False,
                 equipamento_caro=False, calcao=False, recorrente=False):
        self.ferramenta = ferramenta
        self.dias = dias
        self.entrega = entrega
        self.retirada = retirada
        self.atraso = atraso
        self.danificado = danificado
        self.sujo = sujo
        self.cancelado = cancelado
        self.cancelamento_24h = cancelamento_24h
        self.equipamento_caro = equipamento_caro
        self.calcao = calcao
        self.recorrente = recorrente

    def calcular_total(self):
        total = 0

        if self.dias > 7:
            total = (self.dias * self.ferramenta.preco) * 0.95
        elif self.dias > 31:
            total = (self.dias * self.ferramenta.preco) * 0.90
        else:
            total = self.dias * self.ferramenta.preco

        if self.cancelado and self.cancelamento_24h:
            return total * 0.10  # apenas taxa de cancelamento aplicada

        if self.entrega:
            total += 50
        if self.retirada:
            total += 50

        if self.atraso > 0:
            total += self.atraso * 1.5 * self.ferramenta.preco

        if self.danificado:
            total += 300

        if self.sujo:
            total += 50
            #esse de baixo é tipo assim
            # se o produto for caro e isso for o calçao sendo cobrado int o total é esse
        if self.equipamento_caro:
            if self.calcao:
                total += self.ferramenta.preco * self.dias * 0.20  # 20%
        if self.recorrente:
            total = total * 0.85


        return total
class estoque:
    def __init__(self, nome, quantidade, disponivel):
        self.nome = nome
        self.quantidade = quantidade
        self.disponivel = disponivel

    def __str__(self):
        return f"{self.nome} | Quantidade: {self.quantidade} | Disponível: {self.disponivel}"

class mostrar_estoque:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def mostrar_estoque(self):
        if not self.itens:
            print("Estoque vazio.")
        else:
            for item in self.itens:
                print(item)