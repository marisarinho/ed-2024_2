"""
calcular uma expressao pos-fixa
"""
def calcula_expressao(expressao, operandos):
    op = Pilha()
    resultado = 0
    for i in range(len(expressao)):
        if isOperand(expressao[i]):
            op.empilha(operandos[expressao[i]])
        elif expressao[i] == '+':
            for _ in range(2):
                resultado += op.topo()
                op.desempilha()
        elif expressao[i] == '-':
            for _ in range(2):
                resultado -= op.topo()
                op.desempilha()

        elif expressao[i] == '*':
            resultado = 1
            for _ in range(2):
                resultado *= op.topo()
                op.desempilha()
        else:
            v2 = op.topo()
            op.desempilha()
            v1 = op.topo()
            resultado = v1/v2
        op.empilha(resultado)
    return op.topo()