import re

def read_log(name):
    result = []
    not_parsed = []
    pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}|[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:?[0-9a-f]{0,4}:?[0-9a-f]{0,4}) - - \[(\d+/\w+/\d+:\d+:\d+:\d+ [\+-]?\d{4})\] \"(\w+) ([A-Za-z0-9_/]+) ([A-Za-z0-9_/\.]+)\" (\d+) (\d+) \"(.*)\" \"(.*)\"$')
    # pattern = re.compile(r'^([0-9\.]+|[0-9a-f:]+) - - \[(\d+/\w+/\d+:\d+:\d+:\d+ [\+-]?\d{4})\] \"(\w+) ([A-Za-z0-9_/]+) ([A-Za-z0-9_/\.]+)\" (\d+) (\d+) \"(.*)\" \"(.*)\"$')
    with open(name,"rt") as f:
        line = f.readline()
        while (line):
            log = pattern.findall(line)
            if (len(log)):
                result.append((log[0][0], log[0][1], log[0][2], log[0][3], log[0][5], log[0][6]))
            else:
                not_parsed.append(line.strip())
            line = f.readline()
    return result, not_parsed

parsed, not_parsed = read_log("nginx_logs.txt")
print(parsed)
print(not_parsed)
