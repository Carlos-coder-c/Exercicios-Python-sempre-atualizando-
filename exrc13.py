def gerar_resumo_do_pedido(cliente,valor_produto,produto,frete=5, desconto=10):
    subtotal = valor_produto
    total = subtotal + frete - desconto

    print(f"""RESUMO: 
    CLIENTE: {cliente},
    PRODUTO: {produto}, {valor_produto},
    SUBTOTAL: {subtotal}, 
    FRETE: {frete},
    DESCONTO: {desconto},
    TOTAL: {total},
       """)

gerar_resumo_do_pedido(cliente="Carlos", valor_produto=20, produto="Teclado USB")