from threading import Timer


def debounced(func, milliseconds):
    can_call = True

    def reactivate():
        nonlocal can_call
        can_call = True
        
    def debounced_func(*args, **kwargs):
        nonlocal can_call
        if can_call:
            can_call = False
            Timer(milliseconds/1000, reactivate).start()
            return func(*args, **kwargs)
        return

    return debounced_func


if __name__ == '__main__':
    multiply = debounced(lambda x, y: x*y, 200)

    for i in range(1000000):
        x = multiply(2, 3)
        if x is not None:
            print(x)
