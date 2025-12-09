import json


def read_db(file_name):
    with open(file_name, "r") as my_file:
        file_contents = my_file.read()

    file_contents = json.loads(file_contents)
    return file_contents

def write_db(file_name, new_data):
    with open(file_name, "w") as my_file:
        json.dump(new_data, my_file, indent=4)
