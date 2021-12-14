def type_logger(func):
    def wrapper(*arg,**kargs):
        print(f"unnamed agrs count: {len(arg)}")
        for a in arg:
            print(f"{a} : {type(a)}")
        print(f"named agrs count: {len(kargs)}")
        for a in kargs.items():
            print(f"{a[0]} = {a[1]} : {type(a[1])}")
        result = func(*arg,**kargs)
        print(f"result :{result}: {type(result)}")
        return result
    return wrapper

@type_logger
def calc_cube(x,y = 20):
    return x * y

print(calc_cube(10,10.2))
print(calc_cube(10))
print(calc_cube(10,y=2))
print(calc_cube(y=10,x=2))
