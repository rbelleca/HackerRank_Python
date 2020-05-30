def split_and_join(line):
    # Split the string
    split_string = line.split(" ")

    # Join string with hypen
    return '-'.join(split_string)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)