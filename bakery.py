from pathlib import Path
import os

def add(storage, sale):
    id = 0
    try:
        if Path(storage).is_file():
            f = open(storage, "a+t", encoding='utf-8')
        else:
            f = open(storage, "w+t", encoding='utf-8')
        f.seek(0)
        line = f.readline()
        while line:
            record = line.strip().split("\t")
            if record and (2 <= len(record)) and record[0].isnumeric():
                if (int(record[0]) > id):
                    id = int(record[0])
            line = f.readline()
        id = id + 1
        f.write(f"{id}\t{sale}\n")
    finally:
        f.close()
    return id

# def edit(storage, id, sale):
#     buffer = []
#     result = False
#     try:
#         with open(storage, "a+t", encoding='utf-8') as f:
#             f.seek(0)
#             line = f.readline()
#             while line:
#                 record = line.strip().split("\t")
#                 if record and (2 <= len(record)) and record[0].isnumeric():
#                     if (int(record[0]) == id):
#                         buffer.append(f"{id}\t{sale}\n")
#                         result = True
#                     else:
#                         buffer.append(line)
#                 line = f.readline()
#             if (result):
#                 f.truncate(0)
#                 for i in buffer:
#                     f.write(i)
#     except:
#         pass
#     return result

def edit(storage, id, sale):
    bak = f"{storage}.bak"
    result = False
    try:
        if Path(storage).is_file():
            read = open(storage, "rt", encoding='utf-8')
            write = open(bak, "wt", encoding='utf-8')
            line = read.readline()
            while line:
                record = line.strip().split("\t")
                if record and (2 <= len(record)) and record[0].isnumeric():
                    if (int(record[0]) == id):
                        write.write(f"{id}\t{sale}\n")
                        result = True
                    else:
                        write.write(line)
                line = read.readline()
            read.close()
            write.close()
            if (result):
                os.remove(storage)
                os.rename(bak, storage)
            else:
                os.remove(bak)
    except:
        try: read.close()
        except: pass
        try: write.close()
        except: pass
    return result

def show(storage, start = 1, end = -1):
    records = 0
    if Path(storage).is_file():
        with open(storage, "rt", encoding='utf-8') as f:
            line = f.readline()
            while line:
                record = line.strip().split("\t")
                if (2 == len(record)) and (record[0].isnumeric()):
                    id = int(record[0])
                    if (id >= start):
                        if (-1 != end) and (id > end):
                            break
                        records = records + 1
                        print(f"{record[1]}")
                line = f.readline()
    print(f"total records: {records}")
