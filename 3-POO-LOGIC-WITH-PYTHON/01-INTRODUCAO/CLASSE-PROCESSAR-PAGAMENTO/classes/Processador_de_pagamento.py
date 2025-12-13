

class Processador_de_pagamento:
# Método abstrato (simplificado): o usuário só precisa saber que "paga"
    def __init__(self):
        pass
    
    def pagar(self, valor:int, metodo_pagamento:str):
        # Validação básica
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")
        
        match metodo_pagamento:
            case "pix":
               self.__processar_pix(valor)
            case "cartao":
                self.__processar_cartao(valor)
            case _:
                raise ValueError("Método de pagamento inválido. Use 'pix' ou 'cartao'.")
            
    def __processar_pix(self, valor: float) -> dict:
        print(f"[PIX] Processando pagamento de R${valor:.2f}...")
        print("✅ PIX recebido com sucesso!")
        return {"sucesso": True, "metodo": "pix", "valor": valor}

    def __processar_cartao(self, valor: float) -> dict:
        print(f"[CARTÃO] Validando transação de R${valor:.2f}...")
        print("✅ Pagamento com cartão aprovado!")
        return {"sucesso": True, "metodo": "cartao", "valor": valor}