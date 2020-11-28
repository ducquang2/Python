if __name__ == '__main__':
    n = int(input())

    # t = tuple(int(i) for i in input().split())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))