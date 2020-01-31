data = 'Hello World!'


class Reader:

    def __init__(self, data):
        self.data = data
        self.current = 0
        self.buffer = []
    
    def read7(self):
        stop = min(self.current + 7, len(self.data))
        result = data[self.current:stop]
        self.current += stop
        return result

    def readN(self, n):
        result = ''
        if len(self.buffer) > 0:
            stop = min(len(self.buffer), n)
            result += self.buffer[:stop]
            n -= stop
        while n > 0:
            self.buffer = self.read7()
            if len(self.buffer) == 0:
                break
            stop = min(len(self.buffer), n)
            result += self.buffer[:stop]
            self.buffer = self.buffer[stop:]
            n -= stop
        return result


if __name__ == '__main__':
    r = Reader(data)
    print('Calling read7() thrice: ')
    print(f'"{r.read7()}"')
    print(f'"{r.read7()}"')
    print(f'"{r.read7()}"')
    print()
    r = Reader(data)
    aux = 0
    while True:
        try:
            aux = int(input('Read how many characters? (99 to stop): ').strip())
        except ValueError:
            continue
        if aux == 99:
            break
        print(f'"{r.readN(aux)}"')
