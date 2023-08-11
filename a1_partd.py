from a3_maze import Maze

def find_path(maze: Maze, from_cell: int, to_cell: int) -> list:
    """
    Finds a path from the starting cell to the goal cell within the maze.

    Args:
        maze (Maze): An instance of the Maze class representing the maze.
        from_cell (int): The cell number representing the starting cell.
        to_cell (int): The cell number representing the goal cell.

    Returns:
        list: A list of cell numbers representing the path from the starting cell to the goal cell.
              An empty list if no path is found.
    """
    result = helper(maze, from_cell, to_cell, [])
    if not result:
        return []
    return result


def helper(maze: Maze, from_cell: int, to_cell: int, path: list):
    """
    Recursive helper function to find the path within the maze.

    Args:
        maze (Maze): An instance of the Maze class representing the maze.
        from_cell (int): The cell number representing the current cell.
        to_cell (int): The cell number representing the goal cell.
        path (list): A list representing the current path.

    Returns:
        Union[list, bool]: A list of cell numbers representing the path from the starting cell to the goal cell.
                           False if no path is found.
    """
    if from_cell == to_cell:
        # Found the goal cell, returning the path
        path.append(to_cell)
        return path

    path_copy = path[:]

    right = maze.get_right(from_cell)
    if (right != -1) and not maze.get_is_marked(right):
        maze.mark_cell(from_cell)
        path_copy.append(from_cell)
        right = helper(maze, right, to_cell, path_copy)
        if right:
            return right

    path_copy = path[:]

    down = maze.get_down(from_cell)
    if (down != -1) and not maze.get_is_marked(down):
        maze.mark_cell(from_cell)
        path_copy.append(from_cell)
        down = helper(maze, down, to_cell, path_copy)
        if down:
            return down

    path_copy = path[:]

    left = maze.get_left(from_cell)
    if (left != -1) and not maze.get_is_marked(left):
        maze.mark_cell(from_cell)
        path_copy.append(from_cell)
        left = helper(maze, left, to_cell, path_copy)
        if left:
            return left

    path_copy = path[:]

    up = maze.get_up(from_cell)
    if (up != -1) and not maze.get_is_marked(up):
        maze.mark_cell(from_cell)
        path_copy.append(from_cell)
        up = helper(maze, up, to_cell, path_copy)
        if up:
            return up

    # None of the paths at the cell lead to the goal cell
    return False
