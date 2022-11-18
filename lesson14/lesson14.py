def my_sum(*args):
    s = 0
    if not args:
        return None

    for i in args:
        try:
            float(i)
        except:
            return "error"
        if i % 2:
            s += i
        else:
            s += i ** 2
    return s


def sum_rows(matrix):
    result = []
    for row in matrix:
        result.append(my_sum(*row))
    return result
