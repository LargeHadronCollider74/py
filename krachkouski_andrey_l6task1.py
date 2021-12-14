def read_log(name):
    result = []
    with open(name,"rt") as f:
        line = f.readline()
        while (line):
            ip = None
            querytype = None
            query = None
            end = line.find(" - -")
            if (-1 < end):
                ip = line[0:end]
            start = line.find('] "')
            end = -1
            if (-1 < start):
                start = start + 3
                end = line.find('"', start)
            if (-1 < start) and (-1 < end):
                query = line[start:end]
            if (query):
                end = query.find(" ")
                if (-1 < end):
                    querytype = query[0:end]
                    query = query[end + 1:]
            if (ip and querytype and query):
                result.append((ip, querytype, query));
            line = f.readline()
    return result

res = read_log("nginx_logs.txt")
print(res)