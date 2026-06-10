def prim_algoritmo(vertices, edges):
    adj_list = {v: [] for v in vertices}
    for u, v, weight in edges:
        adj_list[u].append((v, weight))
        adj_list[v].append((u, weight))

    mst_edges = []
    included = set()
    total_cost = 0

    import heapq
    pq = [(0, vertices[0], None)] 

    while pq and len(included) < len(vertices):
        weight, current, previous = heapq.heappop(pq)
        if current not in included:
            included.add(current)
            if previous is not None:
                mst_edges.append((previous, current, weight))
                total_cost += weight

            for neighbor, w in adj_list[current]:
                if neighbor not in included:
                    heapq.heappush(pq, (w, neighbor, current))

    return mst_edges, total_cost

def processa_prim_arquivo(entrada, saida):
    with open(entrada, 'r') as file:
        lines = file.readlines()
        vertices = lines[0].strip().split(',')
        edges = []
        for line in lines[1:]:
            u, v, weight = line.strip().split(',')
            edges.append((u, v, int(weight)))

    arestas, custo = prim_algoritmo(vertices, edges)

    with open(saida, 'w', encoding='utf-8') as file:
        file.write("Arvore Geradora de Peso Minimo - Prim\n")
        file.write("Arestas:\n")
        for u, v, peso in arestas:
            file.write(f"{u} - {v}: {peso}\n")
        file.write(f"\nCusto Total: {custo}\n")

input_file = "arquivoentra.txt"
output_file = "ResultadoPrim.txt"

processa_prim_arquivo(input_file, output_file)