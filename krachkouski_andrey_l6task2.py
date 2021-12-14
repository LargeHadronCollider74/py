def get_often_ip(name):
    dict = {}
    with open(name,"rt") as f:
        line = f.readline()
        while (line):
            pos = line.find(" - -")
            if (-1 < pos):
                ip = line[0:pos]
                count = 0
                if ip in dict:
                    count = dict[ip]
                dict[ip] = count + 1
            line = f.readline()
    if (0 == len(dict)):
        return None
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)[0][0]

print(get_often_ip("nginx_logs.txt"))