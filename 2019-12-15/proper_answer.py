challenge_input = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

# --- for testing ---
order = {
        'R': 1,
        'G': 2,
        'B': 3
    }


def batteries_included_sort(input_list):
    l = input_list[:]
    return sorted(l, key=lambda x: order[x])
# --- for testing ---


def update_offsets(found):
    return {
            'R': found['R'],
            'G': found['R'] + found['G'],
            'B': found['R'] + found['G'] + found['B']
        }


def rgb_sort(input_list):
    l = input_list[:]
    found = {
            'R': 0,
            'G': 0,
            'B': 0
        }
    offset = update_offsets(found)
    for i in range(len(l)):
        val = l[i]
        if val == 'R':
            l[i], l[offset['R']] = l[offset['R']], l[i]
        if val == 'R' or val == 'G':
            l[i], l[offset['G']] = l[offset['G']], l[i]
        found[val] += 1
        offset = update_offsets(found)
    return l


if __name__ == '__main__':
    rgb_sorted = rgb_sort(challenge_input)
    correctly_sorted = batteries_included_sort(challenge_input)
    assert rgb_sorted == correctly_sorted, 'Sort not working: {}'.format(rgb_sorted)
    print('It works!: {}'.format(rgb_sorted))
    
