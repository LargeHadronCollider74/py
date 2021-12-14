import sys

def odd_nums(max):
    for i in range(1, max + 1, 2):
        yield i

gen = odd_nums(20)
print(type(gen), sys.getsizeof(gen))
print(next(gen))
for i in gen:
    print(i)
