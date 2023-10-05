if __name__ == "__main__":
    import hidden_4

    # Get the names defined in the module
    names = dir(hidden_4)

    # Filter and sort the names
    filtered_names = sorted([name for name in names if not name.startswith("__")])

    # Print the names, one per line
    for name in filtered_names:
        print(name)
