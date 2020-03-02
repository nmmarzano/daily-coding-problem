def sort_string(w):
    return ''.join(sorted(list(w)))


def find_anagram_indices(w, s):
    sorted_w = sort_string(w)
    results = []
    
    for i in range(len(s) - len(w) + 1):
        if sorted_w == sort_string(s[i:i+len(w)]):
            results.append(i)

    return results;


if __name__ == '__main__':
    w = input('Enter word to find anagrams of: ').strip()
    s = input('Enter string to search for anagrams: ').strip()
    print(find_anagram_indices(w, s))
    
