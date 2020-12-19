import os


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("File does not exist")


def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
    else:
        print("File does not exist")


def create_file(filename):
    if os.path.exists(filename):
        return
    with open(filename, 'w'):
        pass
