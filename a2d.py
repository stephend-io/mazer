class Graph:
    def __init__(self, num_verts):
        self.count_vertices = num_verts
        self.count_edges = 0
        self.list_adj = [[] for _ in range(num_verts)]

    def add_vertex(self):
        self.count_vertices += 1
        self.list_adj.append([])

    def add_edge(self, idx_from, idx_to, weight=1):
        if idx_from < 0 or idx_from >= self.count_vertices or idx_to < 0 or idx_to >= self.count_vertices:
            return False
        for edge in self.list_adj[idx_from]:
            if edge[0] == idx_to:
                return False
        self.list_adj[idx_from].append((idx_to, weight))
        self.count_edges += 1
        return True

    def num_edges(self):
        return self.count_edges

    def num_verts(self):
        return self.count_vertices

    def has_edge(self, idx_from, idc_to):
        if idx_from < 0 or idx_from >= self.count_vertices or idc_to < 0 or idc_to >= self.count_vertices:
            return False
        for edge in self.list_adj[idx_from]:
            if edge[0] == idc_to:
                return True
        return False

    def edge_weight(self, idx_from, idx_to):
        if idx_from < 0 or idx_from >= self.count_vertices or idx_to < 0 or idx_to >= self.count_vertices:
            return None
        for edge in self.list_adj[idx_from]:
            if edge[0] == idx_to:
                return edge[1]
        return None

    def get_connected(self, x):
        if x < 0 or x >= self.count_vertices:
            return None
        conn_verts = []
        for edge in self.list_adj[x]:
            conn_verts.append((edge[0], edge[1]))
        return conn_verts
