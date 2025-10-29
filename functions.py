FILEPATH = "todos.txt"

def read_list(filepath=FILEPATH):
    """ Read a text file and return the list of
     to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_list(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file."""
    with open(filepath, "w") as w_list:
        w_list.writelines(todos_arg)