import sys


def can_become_nondecreasing(arr):
    if len(arr) == 1 or len(arr) == 2:
        return True

    cpy_arr = arr[::]
    aux = [-1, -1, sys.maxsize]
    count = 0
    for i in range(len(arr)):
        aux[0] = cpy_arr[i - 1] if i - 1 >= 0 else -1
        aux[1] = cpy_arr[i]
        aux[2] = cpy_arr[i + 1] if i + 1 < len(cpy_arr) else sys.maxsize

        if aux[0] <= aux[2] and (aux[1] < aux[0] or aux[1] > aux[2]):
            count += 1
            cpy_arr[i] = aux[0] if aux[0] > -1 else aux[2]

    print(f'Resulting array: {cpy_arr}')
    return count <= 1


if __name__ == '__main__':
    data = []
    while True:
        num = int(input('Enter a number (-1 to stop): ').strip())
        if num < 0 or num >= sys.maxsize:
            break
        data.append(num)
    print()
    print(can_become_nondecreasing(data))
