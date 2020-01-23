import cProfile

def naive_count(n, x):
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i*j == x:
                count += 1
    return count


def fast_count(n, x):
    count = 0
    mult = 0
    for i in range(1, n + 1):
        # end quick if i is bigger than the value
        # no multiplication will yield it anymore
        if i > x:
            break
        # matrix is symmetric so I only need to check the upper half
        for j in range(i, n + 1):
            mult = i*j
            # break out once the value has been found or surpassed
            # values will only grow from now on
            if mult >= x:
                # when value is found:
                # add 1 to count if I'm on the diagonal
                # add 2 to account for the symmetry otherwise
                if mult == x:
                    if i == j:
                        count += 1
                    else:
                        count += 2
                break
    return count


if __name__ == '__main__':
    n = int(input('N: ').strip())
    x = int(input('X: ').strip())

    naive_c = 0
    fast_c = 0

    cProfile.run('naive_c = naive_count(n, x)')
    print(f'Naive count: {naive_c}\n')
    cProfile.run('fast_c = fast_count(n, x)')
    print(f'Fast count: {fast_c}\n')
