class Node:
    def __init__(self, val='', child=None):
        self.val = val
        self.child = child

    def get_child(self):
        return self.child

    def set_child(self, node):
        self.child = node

    def __repr__(self):
        return f'{{val: {self.val}, child:{type(self.child)}}}'


def reverse_list(ll):
    cur = ll
    nxt = cur.get_child()
    aux = nxt.get_child() if nxt is not None else None
    cur.set_child(None)
    while True:
        if nxt is not None:
            nxt.set_child(cur)
        else:
            break
        
        cur = nxt
        nxt = aux
        if nxt is not None:
            aux = nxt.get_child()
            
    return cur


def print_list(ll):
    cur = ll
    while cur is not None:
        print(cur)
        cur = cur.get_child()


def create_list(length):
    head = Node(1)
    cur = head
    for i in range(2, length + 1):
        aux = Node(i)
        cur.set_child(aux)
        cur = aux
    return head
        

if __name__ == '__main__':
    length = int(input('Enter length of list: ').strip())
    ll = create_list(length)

    print('\nList: ')
    print_list(ll)
    print('\nReversed: ')
    ll = reverse_list(ll)
    print_list(ll)
