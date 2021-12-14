class Storage():
    def __init__(self, name):
        self.name = name
        self.storage = {}
    def push(self, item):
        if item.name in self.storage:
            self.storage[item.name].append(item)
        else:
            self.storage[item.name] = [item]
    def pushany(self, itemname, count):
        try:
            count = int(count)
            if (0 >= count):
                raise ValueError("count must be positive integer value, more than 0")
            if "Printer" == itemname:
                while 0 < count:
                    self.push(Printer(False))
                    count = count - 1
            elif "Scanner" == itemname:
                while 0 < count:
                    self.push(Scanner("manual"))
                    count = count - 1
            elif "Copyer" == itemname:
                while 0 < count:
                    self.push(Copyer("A4"))
                    count = count - 1
            return True
        except ValueError as e:
            print(e)
            return False
    def pop(self, itemname):
        if itemname in self.storage:
            if 0 < len(self.storage[itemname]):
                result = self.storage[itemname][-1]
                self.storage[itemname].remove(result)
                return result
        return None
    def move_to(self, itemname, storage, count = 1):
        while 0 < count:
            item = self.pop(itemname)
            if not item:
                return False
            storage.push(item)
            count = count - 1
        return True
    def __str__(self):
        result = f"{self.name}\n"
        result = result + "\n".join(f"{x} - {len(self.storage[x])}" for x in self.storage.keys())
        return result

class Item():
    def __init__(self, name):
        self.name = name

class Printer(Item):
    def __init__(self, haveUTPconnection):
        Item.__init__(self, "Printer")
        self.haveUTPconnection = haveUTPconnection

class Scanner(Item):
    def __init__(self, type):
        Item.__init__(self, "Scanner")
        self.type = type

class Copyer(Item):
    def __init__(self, maxpapersize):
        Item.__init__(self, "Copyer")
        self.maxpapersize = maxpapersize


storage = Storage("storage")
bosses = Storage("bosses")
accounts = Storage("accounts")

storage.push(Printer(True))
storage.push(Printer(True))
storage.pushany("Printer", 2)
storage.push(Scanner("auto"))
storage.pushany("Scanner", "5")
storage.push(Copyer("A3"))
storage.push(Copyer("A2"))
storage.pushany("Copyer", "1")
print(storage)
print(bosses)
print(accounts)

item = storage.pop("Printer")
if item:
    bosses.push(item)
storage.move_to("Scanner", bosses, 2)
storage.move_to("Copyer", accounts, 3)
print(storage)
print(bosses)
print(accounts)
