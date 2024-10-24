def fazer_pedido(quant:int,produto,carrinho,total_compras):
    subtotal=produto["valor"] * quant
    total_compras += subtotal
    carrinho.append({
            "descricao": produto["descricao"],
             "valor": produto["valor"],
            "quantidade": quant,
        })
    return total_compras