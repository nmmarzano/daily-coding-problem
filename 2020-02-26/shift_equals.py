def shift_equals(a, b):
    if len(a) != len(b):
        return False

    if a == b:
        return True
    
    for i in range(len(a) - 1):
        a = a[-1] + a[:-1]
        if a == b:
            return True

    return False


if __name__ == '__main__':
    print(shift_equals('abcde', 'cdeab'))
    print(shift_equals('abc', 'acb'))
