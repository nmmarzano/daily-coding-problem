data = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}


def combinations(data, numbers):
    first = numbers[0]
    second = numbers[1]
    result = []
    for c1 in data[first]:
        for c2 in data[second]:
            result.append(''.join([c1, c2]))
    return result


def get_numbers_in_range(r):
    while True:
        x = input(f'Enter number in range {r.start}-{r.stop-1}: ')
        try:
            aux = int(x)
        except ValueError:
            continue
        if aux < 100 and aux // 10 in r and aux % 10 in r:
            break
    print(f'Accepted string "{x}"')
    return x


if __name__ == '__main__':
    x = get_numbers_in_range(range(2, 10))
    print(f'Result: {combinations(data, x)}')
