board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]


def exists(board, word):
    word = word.upper()
    for line in board:
        for letter in line:
            if letter in word:
                index = word.index(letter)
                word = word[:index] + word[index+1:]
            if len(word) == 0:
                return True
    return False


if __name__ == '__main__':
    print(exists(board, "ABCCED"))
    print(exists(board, "SEE"))
    print(exists(board, "ABCB"))
                
