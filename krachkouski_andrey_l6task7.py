import bakery.bakery as bakery
import sys

command = ""
start = 1
end = -1
id = 0
sale = None
filename = "bakery.csv"
argcount = len(sys.argv)

if (2 <= argcount):
    if (1 == len(sys.argv[1])):
        if (sys.argv[1] in ("s", "a", "e")):
            command = sys.argv[1]
if (0 == sys.argv[len(sys.argv) - 1].find("-f")):
    filename = sys.argv[len(sys.argv) - 1][2:]
    argcount = argcount - 1
if ("a" == command) and (3 <= argcount):
    try:
        sale = float(sys.argv[2])
    except:
        command = ""
        print(f"wrong command line")
if ("e" == command) and (4 <= argcount):
    try:
        id = int(sys.argv[2])
        sale = float(sys.argv[3])
    except:
        command = ""
        print(f"wrong command line")
if ("s" == command) and (3 <= argcount):
    try:
        start = int(sys.argv[2])
        if (0 >= start):
            raise ValueError
    except:
        command = ""
        print(f"wrong command line")
if ("s" == command) and (4 <= argcount):
    try:
        end = int(sys.argv[3])
        if (start >= end):
            raise ValueError
    except:
        command = ""
        print(f"wrong command line")

if (command):
    # print(f"command {command}, start {start}, end {end}, id {id}, sale {sale}, filename {filename}")
    if ("s" == command):
        bakery.show(filename, start, end)
    elif ("a" == command):
        print(f"Added record id = {bakery.add(filename, sale)}")
    elif ("e" == command):
        print(f"Edit record id {id} is successful: {bakery.edit(filename, id, sale)}")
else:
    print('Using: "l6 task5.py" <command> [<arguments>...] [<switch>]')
    print('commands:')
    print(' s [start [end]]')
    print('  show sales from start to end records')
    print(' a sale')
    print('  add sale')
    print(' e record_id sale')
    print('  edit sale')
    print('switch:')
    print(' -f<filename>')
    print('  filename')

