import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['{}={}'.format(k, v) for k, v in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('{} {}({}) -> {}'.format(elapsed, func.__name__, arg_str, result))
        return result

    return clocked


@clock
def million():
    for i in range(1000000):
        pass


@clock
def snooze(n):
    time.sleep(n)


million()
snooze(n=2)
print(million.__name__)
