lst = [9, 12, 3, 9, 5, 5, 3, 14, 10, 9, 10]


def pivot_sort_multiple_lists(lst, pivot):
    lesser = []
    equal = []
    bigger = []

    for num in lst:
        if num < pivot:
            lesser.append(num)
        elif num == pivot:
            equal.append(num)
        elif num > pivot:
            bigger.append(num)

    return lesser + equal + bigger
        

def pivot_sort_in_place(lst, pivot):
    cpy = lst[:]
    pivot_position = 0

    for i in range(len(cpy)):
        if cpy[i] == pivot or i == len(cpy) - 1:
            pivot_position = i
            j = 0
            while j < pivot_position:
                if cpy[j] > pivot:
                    cpy = cpy[:j] + cpy[j+1:] + [cpy[j]]
                    pivot_position -= 1
                elif cpy[j] == pivot:
                    cpy = cpy[:j] + cpy[j+1:]
                    cpy = cpy[:pivot_position] + [pivot] + cpy[pivot_position:]
                    j += 1
                else:
                    j += 1
            j += 1
            while j < len(cpy):
                if cpy[j] < pivot:
                    cpy = [cpy[j]] + cpy[:j] + cpy[j+1:]
                    pivot_position += 1
                elif cpy[j] == pivot:
                    cpy = cpy[:j] + cpy[j+1:]
                    cpy = cpy[:pivot_position] + [pivot] + cpy[pivot_position:]
                    j += 1
                else:
                    j += 1
            break
    return cpy
    

if __name__ == '__main__':
    print(f'input list: {lst}')
    print()

    pivot = 0
    while True:
        pivot = int(input('Enter the pivot (99 to stop): ').strip())
        if pivot == 99:
            break
        print()
        print('pivot_sort_multiple_lists:')
        print(pivot_sort_multiple_lists(lst, pivot))
        print()
        print('pivot_sort_in_place:')
        print(pivot_sort_in_place(lst, pivot))
        print()
