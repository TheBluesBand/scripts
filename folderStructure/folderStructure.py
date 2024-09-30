import os

def print_structure(path, level=0, is_last=False):
    """
    Prints the directory structure of a path with indentation and vertical lines.

    Args:
        path: The path to the directory.
        level: The current indentation level (0-based).
        is_last: True if the current item is the last child of its parent.
    """
    indent = "  " * level
    corner = "└── " if is_last else "├── "
    vertical_line = "│  " if level > 0 and not is_last else "   "

    print(f"{indent}{vertical_line}{corner}{os.path.basename(path)}")

    if os.path.isdir(path):
        for i, item in enumerate(os.listdir(path)):
            child_path = os.path.join(path, item)
            is_last_child = (i == len(os.listdir(path)) - 1)
            print_structure(child_path, level + 1, is_last_child)

def main():
    # Get the directory path from the user
    directory_path = input("Enter the directory path: ")
    print_structure(directory_path)

if __name__ == "__main__":
    main()