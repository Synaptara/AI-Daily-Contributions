def check_file_exists(filename):
    try:
        # attempt to open the file in read mode
        with open(filename, 'r') as file:
            # if no exception occurs, the file exists and can be opened
            return True
    except OSError:
        # any OS-related exception indicates the file does not exist or cannot be opened
        return False