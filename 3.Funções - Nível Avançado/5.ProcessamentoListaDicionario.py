def produto_mais_caro(produtos):
    if not produtos:
        return None
    
    mais_caro = produtos[0]

    for produto in produtos:
        if produto['preco'] > mais_caro['preco']:
            mais_caro = produto
    
    return mais_caro
    
estoque = [
    {"nome": "Teclado", "preco": 150.00},
    {"nome": "Monitor", "preco": 1200.00},
    {"nome": "Mouse", "preco": 80.00},
    {"nome": "Notebook", "preco": 4500.00},
    {"nome": "Placa de Vídeo", "preco": 15000.00}
]

vencedor = produto_mais_caro(estoque)
print(f"O produto mais caro é {vencedor['nome']}, custando {vencedor['preco']}")