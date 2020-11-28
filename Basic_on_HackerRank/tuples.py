if __name__ == '__main__':
    n = int(input())
    t = tuple(int(i) for i in input().split())
    print(hash(t))