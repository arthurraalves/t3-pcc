from DirectedEdge import DirectedEdge
from Digraph import Digraph
from DirectedEulerianCycle import DirectedEulerianCycle


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()

    V = int(linhas[0])
    E = int(linhas[1])

    mapa = {}
    contador = 0

    arestas = []

    for linha in linhas[2:]:
        v, w, peso = linha.split()
        peso = int(peso)

        if v not in mapa:
            mapa[v] = contador
            contador += 1
        if w not in mapa:
            mapa[w] = contador
            contador += 1

        arestas.append((v, w, peso))

    g = Digraph(V)

    for v, w, peso in arestas:
        edge = DirectedEdge(mapa[v], mapa[w], peso)
        g.add_edge(edge)

    return g, mapa, arestas


def calcular_custo(caminho, arestas, mapa):
    custo = 0
    inv = {v: k for k, v in mapa.items()}

    for i in range(len(caminho) - 1):
        v = inv[caminho[i]]
        w = inv[caminho[i + 1]]

        for a, b, peso in arestas:
            if a == v and b == w:
                custo += peso
                break

    return custo


def main():
    arquivo = "C:\\Users\\arthu\\Downloads\\t3-pcc\\dados\\entrada_eulerizada.txt"

    g, mapa, arestas = ler_arquivo(arquivo)

    print("Graus dos vértices:")
    for k, v in mapa.items():
        print(f"{k}: entrada={g.in_degree[v]}, saída={g.out_degree[v]}")

    if not g.is_balanced():
        print("\nGrafo NÃO balanceado!")
        return

    print("\nGrafo balanceado! Executando Hierholzer...\n")

    euler = DirectedEulerianCycle(g)
    ciclo = euler.get_cycle()

    inv = {v: k for k, v in mapa.items()}
    caminho = [inv[v] for v in ciclo]

    print("Circuito Euleriano:")
    print(" -> ".join(caminho))

    custo = calcular_custo(ciclo, arestas, mapa)

    print(f"\nCusto total: {custo}")


if __name__ == "__main__":
    main()