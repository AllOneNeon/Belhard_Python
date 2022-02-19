def inspect (func: int) -> None:
    def wrapper (*args, **kwargs):
        res = func (*args, **kwargs)
        return res
    return wrapper

# функция, которая оборачивается

@inspect
def concat (n):
    l = [x for x in range(n) if x % 2 == 0]
    return l
print (concat(10))