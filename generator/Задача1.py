def number_sequence(n):
    for i in range(1, n + 1):
        yield i

if __name__ == '__main__':
    for i in number_sequence(10):
        print(i)