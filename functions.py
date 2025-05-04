def get_todos(filepath="todos.txt"):
    # Are referred to as docstring
    """ Read a text file and return
    a list of to-dos item
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-dos items to the text file """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

#value of __name__ will be the name of this file i.e. functions when called by another script e.g. cli.py
#print(__name__)

# value of __name__ will be equal to "__main__" if call from within this script e.g, functions.py
if __name__ == "__main__":
    print("Executing from the functions.py script")