from a3_parta import MinHeap


def minimum_spanning_tree(graph):    #prim
    mst = []  # List to store minimum spanning tree edges
    visit = set()  # Set of visit vertices
    
    # Create a MinHeap to store edges
    edge_heap = MinHeap([(0, None, 0)])    #edge_heap becomes a minHeap array and heapify down ||weight from, to

    while not edge_heap.is_empty():
        weight, curr_ver, next_vert = edge_heap.extract_min()    #extract min value from heap and remove it

        if next_vert not in visit:                       #if not visit
            visit.add(next_vert)                         #turn into visit
            if curr_ver is not None:                        
                mst.append((curr_ver, next_vert))       #save MST excluding starter

            for neighbor, weight in graph.get_connected(next_vert): #check neighbours and value if visted
                if neighbor not in visit:
                    edge_heap.insert((weight, next_vert, neighbor))

    return mst
