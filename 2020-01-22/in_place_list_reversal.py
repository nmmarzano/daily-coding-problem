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
        

if __name__ == '__main__':
    n5 = Node('5')
    n4 = Node('4', n5)
    n3 = Node('3', n4)
    n2 = Node('2', n3)
    n1 = Node('1', n2)

    ll = n1

    print_list(ll)
    print()
    ll = reverse_list(ll)
    print_list(ll)
