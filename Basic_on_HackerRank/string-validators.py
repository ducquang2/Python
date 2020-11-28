if __name__ == '__main__':
    s = input()
    print(any(temp.isalnum() for temp in s))
    print(any(temp.isalpha() for temp in s))
    print(any(temp.isdigit() for temp in s))
    print(any(temp.islower() for temp in s))
    print(any(temp.isupper() for temp in s))