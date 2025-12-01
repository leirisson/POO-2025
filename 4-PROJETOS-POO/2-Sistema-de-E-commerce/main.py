from classes.ProdutoFisico import ProdutoFisico
from classes.ProdutoDigital import ProdutoDigital


def main():
    livro_fisico = ProdutoFisico("Python para Iniciantes", 50, 0.5)
    ebook = ProdutoDigital("Python Avançado", 30, 15)
    
    livro_fisico.adicionar_produto_no_estoque(10)
    ebook.adicionar_produto_no_estoque(1000)
    
    # Polimorfismo em ação
    carrinho = [
    (livro_fisico, 2),
    (ebook, 6)
    ]
    
    total = 0
    
    for produto, qtd in carrinho:
        valor = produto.calcular_total(qtd)
        print(f"{produto.nome}: R${valor:.2f}")
        total += valor

    print(f"Total: R${total:.2f}")

if __name__ == "__main__":
    main()