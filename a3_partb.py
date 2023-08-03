from a3_parta import MinHeap


def minimum_spanning_tree(graph):
    visited_nodes = set()
    heap = MinHeap()

    start_node = 0
    visited_nodes.add(start_node)
    for neighbor, weight in graph.get_connected(start_node):
        heap.insert((weight, start_node, neighbor))

    mst = []
    while heap and len(visited_nodes) < graph.num_verts():
        weight, node1, node2 = heap.extract_min()

        if node1 not in visited_nodes or node2 not in visited_nodes:
            mst.append((node1, node2))

            if node1 in visited_nodes:
                visited_nodes.add(node2)
                current_node = node2
            else:
                visited_nodes.add(node1)
                current_node = node1

            for neighbor, weight in graph.get_connected(current_node):
                if neighbor not in visited_nodes:
                    heap.insert((weight, current_node, neighbor))

    return mst
