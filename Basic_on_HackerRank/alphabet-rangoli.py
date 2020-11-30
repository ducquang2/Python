def print_rangoli(size):
    # your code goes here
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]

    for i in range(size-1, -size, -1):
        x = abs(i)
        line = myStr[size:x:-1] + myStr[x:size]
        print("--"*x + '-'.join(line) + "--"*x)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
