from a3_maze import Maze


def find_path(the_maze, from_cell, to_cell):
    if (from_cell == to_cell):
        return [from_cell]

    the_maze.mark_cell(from_cell)

    def mark(neighbour):
        if the_maze.get_is_marked(neighbour) == False:
            return True

    def equal_cell(neighbour):
        if (neighbour == to_cell):
            return [from_cell, neighbour]

    to_right = the_maze.get_right(from_cell)
    if (to_right != -1 and mark(to_right)):
        equal_cell(to_right)
        path = find_path(the_maze, to_right, to_cell)
        if path:
            path = [from_cell] + path
            return path

    to_left = the_maze.get_left(from_cell)
    if (to_left != -1 and mark(to_left)):
        equal_cell(to_left)
        path = find_path(the_maze, to_left, to_cell)
        if path:
            path = [from_cell] + path
            return path

    to_up = the_maze.get_up(from_cell)
    if (to_up != -1 and mark(to_up)):
        equal_cell(to_up)
        path = find_path(the_maze, to_up, to_cell)
        if path:
            path = [from_cell] + path
            return path

    to_down = the_maze.get_down(from_cell)
    if (to_down != -1 and mark(to_down)):
        equal_cell(to_down)
        path = find_path(the_maze, to_down, to_cell)
        if path:
            path = [from_cell] + path
            return path

    return []