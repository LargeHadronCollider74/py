import os

def insert_file(dict, file):
    ext = os.path.splitext(file)[1]
    ext = ext[1:] if (-1 < ext.find(".")) else ext
    ext = ext if (0 < len(ext)) else None
    size = os.path.getsize(file)
    for i in dict:
        if (i > size):
            dict[i][0] = dict[i][0] + 1
            if ext not in dict[i][1]:
                dict[i][1].append(ext)
            return
    new_key = list(dict.keys())[0]
    while size > new_key:
        new_key = new_key * 10
        if new_key not in dict:
            dict[new_key] = [0, []]
    dict[new_key] = [1, [ext if ext else None]]

def read_folder(dict, folder):
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if (os.path.isdir(path)):
            read_folder(dict, path)
        else:
            insert_file(dict, path)

def files_rate(folder):
    result = {100: [0, []]}
    read_folder(result, folder)
    for i in result:
        result[i] = tuple(result[i])
    summary = os.path.join(folder, f"{folder}_summary.json")
    with open(summary, "wt") as f:
        f.write("{\n")
        for i in result:
            exts = "', '".join(ext if ext else "None" for ext in result[i][1])
            f.write(f"    {i}: ({result[i][0]}, ['{exts}'])\n")
        f.write("}\n")
    return result

# print(files_rate("d:\\Projects\\Microchip"))
print(files_rate("my_project"))
