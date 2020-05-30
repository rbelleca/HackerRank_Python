# You are given a string .
# Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, 
# digits, lowercase and uppercase characters.


def any_isalnum(string):
    for x in range(len(string)):
        if (string[x].isalnum()): return True
    return False

def any_isalpha(string):
    for x in range(len(string)):
        if (string[x].isalpha()): return True
    return False

def any_isdigit(string):
    for x in range(len(string)):
        if (string[x].isdigit()): return True
    return False

def any_islower(string):
    for x in range(len(string)):
        if (string[x].islower()): return True
    return False

def any_isupper(string):
    for x in range(len(string)):
        if (string[x].isupper()): return True
    return False


if __name__ == '__main__':
    s = input()

    # alphanumeric characters
    print(any_isalnum(s))
    
    # alphabetical characters
    print(any_isalpha(s))

    # digits
    print(any_isdigit(s))

    # lowercase
    print(any_islower(s))

    # uppercase
    print(any_isupper(s))

    
