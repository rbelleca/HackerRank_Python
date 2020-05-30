if __name__ == '__main__':
    n = int(input())
 
    myList = []    
    for _ in range(n):
        name, *args = input().split()
        # print('{0} : {1}'.format(name, type(name)))
        # print('{0} : {1}'.format(args, type(args)))

        args = list(map(int, args))

        if name == 'insert':
            myList.insert(args[0], args[1])
        elif name == 'print':
            print(myList)
        elif name == 'remove':
            myList.remove(args[0])
        elif name == 'append':
            myList.append(args[0])
        elif name == 'sort':
            myList.sort()
        elif name == 'pop':
            myList.pop()
        elif name == 'reverse':
            myList.reverse()
        else:
            None
