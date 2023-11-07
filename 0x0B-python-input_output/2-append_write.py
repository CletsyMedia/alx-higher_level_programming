#!/usr/bin/python3

def append_write(filename="", text=""):
    """Append a string to a text file and return the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added.

    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write(
        "file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
