import random
from a2d import Graph
from a3_partb import minimum_spanning_tree

"""
    Generates a maze with a randomized path 

    Args:
        number_of_rows (int): Number of rows in the maze
        number_of_columns (int): Number of columns in the maze

    Returns:
        list: A list of tuples with each tuple indicating a wall in the maze, to be used by the Maze class
"""
def generate_maze(number_of_rows: int, number_of_columns: int):
    initial_maze = []
    total_walls = number_of_rows * number_of_columns

    # Appends maze tuples, excluding the last column of each row, and the final row at the bottom
    for i in range(total_walls):
        if ((i+1) % number_of_columns!= 0):
            initial_maze.append((i, i+1))
        if (i < total_walls - number_of_columns):
            initial_maze.append((i, i+number_of_columns))

    # Creates a randomized weighted graph from the initial_maze
    graph = Graph(total_walls)
    for wall in initial_maze:
        random_weight = random.randint(1,50)
        graph.add_edge(wall[0], wall[1], random_weight)
        graph.add_edge(wall[1], wall[0], random_weight)

    # Creates walls to be removed from the initial_maze
    mst_hallwaay = minimum_spanning_tree(graph)
    removed_walls = []
    for edge in mst_hallwaay:
        if edge[0] < edge[1]:
            removed_walls.append((edge[0], edge[1]))
        else:
            removed_walls.append((edge[1], edge[0]))

    # Creates final_maze by removing walls of the initial_maze in the walls to be removed
    final_maze= [] 
    for wall in initial_maze:
        if wall not in removed_walls:
            final_maze.append(wall)

    return final_maze
