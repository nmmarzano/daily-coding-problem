import cProfile
        

def naive_pow(x, y):
    if y == 0:
        return 1
    result = x
    for i in range(y - 1):
        result = result * x
    return result


def fast_pow(x, y):
    if y == 0:
        return 1
    result = x
    rest = 1
    while y > 1:
        if y % 2 == 1:
            rest *= result
        result *= result
        y //= 2
    return result * rest


def main():
    base = int(input('Enter base: ').strip())
    power = int(input('Enter power: ').strip())
    print(f'Performing {base}^{power}...\n')
    cProfile.run(f'naive_res = naive_pow({base}, {power})')
    cProfile.run(f'fast_res = fast_pow({base}, {power})')
    if naive_res != fast_res:
        print('ERROR: RESULTS DON\'T MATCH!')
    

if __name__ == '__main__':
    main()
