import math

test = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

order = {
        'R': 1,
        'G': 2,
        'B': 3
    }


def batteries_included_sort(input_list):
    l = input_list[:]
    return sorted(l, key=lambda x: order[x])


def bubble_sort(input_list):
    l = input_list[:]
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if order[l[j]] > order[l[j+1]]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


def selection_sort(input_list):
    l = input_list[:]
    smallest = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            if order[l[j]] < order[l[smallest]]:
                smallest = j
        l[i], l[smallest] = l[smallest], l[i]
    return l


# this one obviously does more than swaps
def merge_sort(input_list):
    l = input_list[:]
    if len(l) == 1:
        return l
    else:
        left = merge_sort(l[:math.floor(len(l)/2)])
        right = merge_sort(l[math.floor(len(l)/2):])
        l = []
        count_l = 0
        count_r = 0
        while count_l < len(left) and count_r < len(right):
            if order[left[count_l]] <= order[right[count_r]]:
                l += left[count_l]
                count_l += 1
            else:
                l += right[count_r]
                count_r += 1
        if count_l < len(left):
            l += left[count_l:]
        if count_r < len(right):
            l += right[count_r:]
    return l


if __name__ == '__main__':
    print(test)
    print(bubble_sort(test))
    print(selection_sort(test))
    print(merge_sort(test))
    print(batteries_included_sort(test))
    
