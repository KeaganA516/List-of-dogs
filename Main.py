"""
Module Docstring: main.py
======================

This is the main module of the read/write to text file project.
"""

__aunthor__ = "Trevor Mcharrah"
__version__ = "O.1"
__date__ = "October 7, 2024"
__license__ = "None"

def read_file(file_name) -> None:
    """
    Reads a file amd prints it to the comsole
    """
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")

def new_file(file_name) -> None:
    """
    Creates a new file and writes data to it, OR overwrites an file.
    """
    with open(file_name, "w") as f:
        f.write("maine coon")

def append_file(file_name, data) -> None:
    """
    appends data to an existing file.
    """
    with open(file_name, "r") as f:
        lines = f.readline()

    with open(file_name, "a") as f:
        f.write("\n")
        f.write(data)

def main():
    """
    Main entry point of the application
    """
    user_submission = input()

    append_file("cats.txt", user_submission )

if __name__ =="__main__":
    """
    Starts the program.
    """
    main()