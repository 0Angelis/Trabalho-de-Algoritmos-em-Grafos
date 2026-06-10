class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(vertices, edges, output_file):
    disjoint_set = DisjointSet(vertices)
    mst_edges = []
    total_cost = 0

    edges.sort(key=lambda x: x[2])  

    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst_edges.append((u, v, weight))
            total_cost += weight

    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Arvore Geradora de Peso Minimo - Kruskal\n")
        file.write("Arestas:\n")
        for u, v, weight in mst_edges:
            file.write(f"{u} - {v}: {weight}\n")
        file.write(f"\nCusto Total: {total_cost}\n")


input_file = "arquivoentra.txt"
output_file = "ResultadoKruskal.txt"

with open(input_file, 'r') as file:
    lines = file.readlines()
    vertices = lines[0].strip().split(',')
    edges = []
    for line in lines[1:]:
        u, v, weight = line.strip().split(',')
        edges.append((u, v, int(weight)))

kruskal(vertices, edges, output_file)
