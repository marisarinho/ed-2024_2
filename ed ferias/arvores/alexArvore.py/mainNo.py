from no import No

def percurso(raiz):
    if raiz is not None:

        percurso(raiz.esq)
        percurso(raiz.dir)
        print(raiz.carga)

raiz = No(10)
raiz.dir = No(6)
raiz.dir.esq = No(7)
raiz.dir.dir = No(8)

percurso(raiz)

