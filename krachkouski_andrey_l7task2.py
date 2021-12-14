import os
import sys
import re

def load_yaml(file):
    result = []
    current = []

    with open(file, "rt") as f:
        line = f.readline()
        while line:
            if (0 == line.strip().find("-")):
                pos = line.find("-")
                text = line[pos + 1:].strip()
                insert = False
                if (pos == len(current)): # increment by 1 only
                    current.append(text)
                    insert = True
                elif (pos < len(current) - 1): # decrement any
                    current = current[0:pos + 1]
                    current[pos] = text
                    insert = True
                elif (pos == len(current) - 1):
                    current[pos] = text
                    insert = True
                if (insert):
                    result.append(tuple(current))
            line = f.readline()
    return result

def create(file, root = ""):
    tree = load_yaml(file)

    for i in tree:
        # path = "\\".join(i)
        path = ""
        for j in i:
            path = os.path.join(path, j)
        if (root):
            path = os.path.join(root, path)
        if re.match(r".*\.\w+$", path):
            with open(path, "wt") as f:
                f.write(f"# {path}")
        else:
            if (not os.path.exists(path)):
                os.mkdir(path)

create("config.yaml")