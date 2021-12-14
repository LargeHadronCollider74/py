import os

def insert_file(dict, size):
    for i in dict:
        if (i > size):
            dict[i] = dict[i] + 1
            return
    new_key = list(dict.keys())[0]
    while size > new_key:
        new_key = new_key * 10
        if new_key not in dict:
            dict[new_key] = 0
    dict[new_key] = 1

def read_folder(dict, folder):
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if (os.path.isdir(path)):
            read_folder(dict, path)
        else:
            insert_file(dict, os.stat(path).st_size)
            # insert_file(dict, os.path.getsize(path))

def files_rate(folder):
    result = {100: 0}
    read_folder(result, folder)
    return result

print(files_rate("my_project"))
