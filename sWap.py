def swap_case(s):
    new_string = ''
    for x in range(len(s)):
        if (s[x].isupper()): new_string += s[x].lower()
        elif (s[x].islower()): new_string += s[x].upper()
        else: new_string += s[x]
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)