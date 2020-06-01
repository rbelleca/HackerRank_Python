# Sample Input
# 17

# Sample Output
#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001    

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary 



def print_formatted(n):
    # Option 1:
    # 0 - represents the first element in format(n)
    # {0:b} - formats the value to have the binary digits only
    width = len("{0:b}".format(n))
    print(bin(n))
    print(width)
    for i in range(1,n+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

    # Option 2:
    # w = len(bin(n)[2:])
    # print(bin(n))
    # print(w)
    # for i in range(1, n+1):
    #     print (str(i).rjust(w,' '), str(oct(i)[2:]).rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '),sep=' ')



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)