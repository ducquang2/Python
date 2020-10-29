if __name__ == '__main__':
    N = int(input())
    output = []
    
    for i in range(0,N):
        ip = input().split()
        if ip[0] == "print":
            print(output)
        elif ip[0] == "insert":
            output.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            output.remove(int(ip[1]))
        elif ip[0] == "pop":
            output.pop()
        elif ip[0] == "append":
            output.append(int(ip[1]))
        elif ip[0] == "sort":
            output.sort()
        else:
            output.reverse()