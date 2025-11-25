from classes.Processador_de_pagamento import Processador_de_pagamento


def main():
    pagamento = Processador_de_pagamento()
    pagamento.pagar(100.00,"pix")
    pagamento.pagar(100.00,"cartao")

if __name__=="__main__":
    main()



    