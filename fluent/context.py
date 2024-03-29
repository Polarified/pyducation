import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write

    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = "Don't divide by zero!"
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("Don't divide by zero!")
            return True


manager = looking_glass()
print(manager)
monster = manager.__enter__()
print(monster)
print(manager)
manager.__exit__(None, None, None)
print(monster)
print('---------------------')
MANAGER = LookingGlass()
print(MANAGER)
MONSTER = MANAGER.__enter__()
print(MONSTER)
print(MANAGER)
MANAGER.__exit__(None, None, None)
print(MONSTER)
