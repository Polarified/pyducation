brackets = {'{': '}', '}': '{', '[': ']', ']': '[', '(': ')', ')': '('}


def is_left_bracket(c):
    return c in ('{', '[', '(')


def is_valid(s):
    stack = []
    for c in s:
        if is_left_bracket(c):
            stack.append(c)
        else:
            if not stack or brackets[stack.pop()] != c:
                return False
    return not stack


def main():
    print(is_valid('{()}'))
    print(is_valid(''))
    print(is_valid('[{[{}()[]]}]()'))


if __name__ == '__main__':
    main()
