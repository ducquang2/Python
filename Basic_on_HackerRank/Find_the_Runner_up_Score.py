if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = 0
    second = 0
    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] < first:
            second = arr[i]
    print(second)