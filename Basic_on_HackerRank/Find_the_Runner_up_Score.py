if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = max(arr)
    second = min(arr)
    for i in range(n):
        if arr[i] > second and arr[i] < first:
            second = arr[i]
    print(second)