import random
from a2d import Graph
from a3_partb import minimum_spanning_tree


def generate_maze(number_of_rows, number_of_columns):
    # Create a list of all walls
    walls = [(i, i + 1) for i in range(number_of_rows * number_of_columns - 1) if (i + 1) % number_of_columns != 0]
    walls += [(i, i + number_of_columns) for i in range(number_of_rows * number_of_columns - number_of_columns)]

    # Create a graph with the given number of vertices
    num_verts = number_of_rows * number_of_columns
    graph = Graph(num_verts)

    # Add edges to the graph for each wall in the list of walls
    for wall in walls:
        weight = random.randint(1, 50)
        graph.add_edge(wall[0], wall[1], weight)
        graph.add_edge(wall[1], wall[0], weight)

    # Find the minimum spanning tree of the graph
    mst = minimum_spanning_tree(graph)

    # Create a list of walls to remove
    walls_to_remove = []
    for edge in mst:
        if edge[0] < edge[1]:
            walls_to_remove.append((edge[0], edge[1]))
        else:
            walls_to_remove.append((edge[1], edge[0]))

    # Remove walls in the list of walls to remove from the original list of walls
    remaining_walls = [wall for wall in walls if wall not in walls_to_remove]

    return remaining_walls
 
