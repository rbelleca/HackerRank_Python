
# Sample Input
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

# import textwrap

def wrap(string, max_width):
    new_string = ''

    for x in range(len(string)):
        if (x == 0): None
        elif (x % max_width == 0):
            new_string += '\n'
        
        new_string += string[x]

            
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)