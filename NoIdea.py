
if __name__ == "__main__":
    
    # Prompt user input 
    # n = total number of integers; m = total number of elements in a set
    n, m = input().split()
    myList = list(map(int, input().split()))
    # print('myList:', myList)

    # Integers I like
    set_A = set(map(int, input().split()))
    # print('set_A:', set_A)

    # Integers I don't like
    set_B = set(map(int, input().split()))
    # print('set_B:', set_B)

    # For each element in myList, if element is in A, plus 1, else minus 1
    happiness = 0
    for x in myList:
        if (x in set_A): happiness += 1
        elif (x in set_B): happiness -= 1

    # Print results
    print (happiness)
