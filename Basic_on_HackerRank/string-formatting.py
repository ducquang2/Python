def print_formatted(number):
    # your code goes here
    spacePad = len(str(bin(number)))
    for i in range(1, number+1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hexa = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])
        formatDecimal = ((" " * (spacePad - len(str(decimal)) - 2)) + decimal) 
        formatOct = ((" " * (spacePad - len(str(octal)) - 2)) + octal) 
        formatHex = ((" " * (spacePad - len(str(hexa)) - 2)) + hexa) 
        formatBin = ((" " * (spacePad - len(str(binary)) - 2)) + binary) 
        print(formatDecimal + " " + formatOct + " " + formatHex + " " + formatBin)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)