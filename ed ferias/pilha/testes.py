# from pilha_seq_mari import Pilha
from pilha_enc_mari import Pilha

# Se for encadeada comnete esseaquió
# pilha = Pilha(10)

# Se for sequencial comente esseaquió
pilha = Pilha()


if hasattr(pilha,  "cheia"):
    if pilha.cheia():
        print("Falhou no teste 1")
        exit()
    print("Passou teste 1")


if pilha.topo() is None:
    print("Falhou no teste 1.5")
    exit()

print("Passou no teste 1.5")

try:
    pilha.desempilha()
    print("Falhou no teste 2")
    exit()
except AssertionError as e:
    print("Passou teste 2")
    
pilha.empilhar(2)
pilha.empilhar(3)

if pilha.topo() != 3:
    print("Falhou no teste 3")
    exit()
print("Passou no teste 3")

if pilha.desempilha() != 3:
    print("Falhou no teste 4")
    exit()
print("Passou no teste 4")

if pilha.topo() != 2:
    print("Falhou no teste 5")
    exit()
print("Passou no teste 5")
