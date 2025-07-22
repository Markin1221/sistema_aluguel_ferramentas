# teste.py

from classes import *

# Criando ferramentas
furadeira = Ferramentas("Furadeira", 100)
serra = Ferramentas("Serra Elétrica", 150)

# Criando estoque
estoque_sistema = mostrar_estoque()
estoque_sistema.adicionar_item(estoque("Furadeira", 10, True))
estoque_sistema.adicionar_item(estoque("Serra Elétrica", 5, True))

print("📦 Estoque atual:")
estoque_sistema.mostrar_estoque()

print("\n📄 Simulando aluguel da Furadeira por 10 dias, com entrega, retirada e 1 dia de atraso:")

# Criando aluguel
aluguel = Aluguel(
    ferramenta=furadeira,
    dias=10,
    entrega=True,
    retirada=True,
    atraso=1,
    danificado=False,
    sujo=True,
    cancelado=False,
    equipamento_caro=True,
    calcao=True,
    recorrente=True  # vai aplicar 15% de desconto no total final
)

valor_total = aluguel.calcular_total()
print(f"💰 Valor total do aluguel: R${valor_total:.2f}")
