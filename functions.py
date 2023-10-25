FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ This is to retrieve the todo file. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ This is to write to the todo file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("This is a function.")
