a = [1, 11, 21, 1211, 111221, ]


def gen_series():
    source = '1'
    series = [source]
    for i in range(30):
        character = ''
        amount = ''
        n = ''
        for c in source:
            if c == character:
                amount += 1
            else:
                n += str(amount) + character
                character = c
                amount = 1
        n += str(amount) + character
        series.append(n)
        source = n
    return series


print(len(gen_series()[30]))
