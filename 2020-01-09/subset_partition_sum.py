from functools import reduce


def serialize_items(in_l):
    return [f'{i}!{x}' for i, x in enumerate(in_l)]


def deserialize_items(in_l):
    l = in_l[:]
    for i in range(len(l)):
            l[i] = int(l[i].split('!')[1])
    return l


def all_subsets(in_set):
    l = in_set[:]
        
    result = [[]]
    aux = result[:]
    for j in range(len(l)):
        new = []
        for i in range(len(l) - j):
            for k in range(len(aux)):
                new_term = [l[i]] + aux[k]
                if l[i] not in aux[k] and set(new_term) not in [set(x) for x in new]:
                    new = new + [new_term]
        result = result + new
        aux = new[:]
        
    return result


def list_difference(list1, list2):
    return list(set(list1).difference(set(list2)))


def sum_list(l):
    return reduce(lambda x,y: x+y, l, 0)


def main():
    input_set  = []
    num = 0
    print('Enter the numbers in the set (enter -1 to end): ')
    while (num := int(input('> ').strip())) != -1:
        input_set.append(num)
        
    input_set = serialize_items(input_set)
    subsets = all_subsets(input_set)
    
    has_two_subsets_with_same_sum = False
    for subset in subsets:
        diff = deserialize_items(list_difference(input_set, subset))
        subset = deserialize_items(subset)
        if sum_list(diff) == sum_list(subset):
            has_two_subsets_with_same_sum = True
            break
        
    print(has_two_subsets_with_same_sum)


if __name__ == '__main__':
    main()
