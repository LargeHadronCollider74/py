def val_checker(val_checker):
    def wrapper(func):
        def _wrapper(*arg, **kargs):
            print(f"unnamed agrs count: {len(arg)}")
            for a in arg:
                print(f"{a} : {type(a)}")
            print(f"named agrs count: {len(kargs)}")
            for a in kargs.items():
                print(f"{a[0]} = {a[1]} : {type(a[1])}")
            val = None
            if (0 < len(arg)):
                val = arg[0]
            if (not val) and ("x" in kargs):
                val = kargs["x"]
            if val and not val_checker(val):
                raise ValueError(f"wrong value: {val}")
            result = func(*arg, **kargs)
            print(f"result :{result}: {type(result)}")
            return result
        return _wrapper
    return wrapper

@val_checker(lambda x: x > 0)
def calc_cube(x=2):
    return x ** 3

print(calc_cube())
print(calc_cube(10))
print(calc_cube(x=-10))
