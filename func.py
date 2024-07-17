FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ read the file and return list of to-do items"""
    with open(filepath, "r") as file_l:
        todos_l = file_l.readlines()
    return todos_l


def write_todos(todos_l, filepath=FILEPATH):
    """write to-do list in the file"""
    with open(filepath, "w") as file_l:
        file_l.writelines(todos_l)
