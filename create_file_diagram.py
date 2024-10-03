# LIBRARIES
# Import the os module, which provides a way to interact with the operating system
import os
from pathlib import Path
from pygments.formatters import ImageFormatter
import pygments.lexers

# FUNCTIONS
def write_to_file(file_name='test.txt', content=''):
    # Open file
    with open(file_name, 'a') as file:
        # Input string to file
        file.write(content)

def is_exist(file_name='test.txt'):
    # Check if file exists
    if os.path.exists(file_name):
        # Remove eisting file
        os.remove(file_name)

def is_hidden(path):
    # Return bool if path is hidden, (hidden paths start with '.')
    return os.path.basename(path).startswith('.')

def generate_diagram(startpath, file_name, prefix=''):
    # scan the repository and create a list of the folders and file.
    repo_list = [e for e in os.scandir(startpath) if not is_hidden(e.path)]
    # Go through repo_list, `enumerate` gets the element and index
    for i, entry in enumerate(repo_list):
        # Check if it the last element
        is_last = (i == len(repo_list) - 1)
        # Chekc if the entry is a directory
        if entry.is_dir():
            # Write Directory
            write_to_file(file_name, f"{prefix}{'└──' if is_last else '├──'} /{entry.name}\n")
            # Recursively call function
            generate_diagram(entry.path, file_name, prefix + ('    ' if is_last else '│   '))
        else:
            # Write File
            write_to_file(file_name, f"{prefix}{'└──' if is_last else '├──'} {entry.name}\n")


# MAIN
def main():
    # get file name
    file_name = "tree.txt"
    # Check if file exist
    is_exist(file_name)
    # Write root node
    write_to_file(file_name, ".\n")
    # Find the root of the repository
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Generate file diagram
    generate_diagram(current_directory, file_name) 
    # Create a lexer for text files
    lexer = pygments.lexers.TextLexer()
    # Get file tree text
    png = pygments.highlight(Path(file_name).read_text(), lexer, ImageFormatter(line_numbers=False))
    # Write File tree to a png
    Path('Default/file_tree_diagram.png').write_bytes(png)
    # Remove text file
    is_exist(file_name)




if __name__ == "__main__":
    main()
