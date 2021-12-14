import sys

def odd_nums(max):
    return (i for i in range(1, max + 1, 2))

gen = odd_nums(20)
print(type(gen), sys.getsizeof(gen), gen.__sizeof__())
print(next(gen))
for i in gen:
    print(i)
