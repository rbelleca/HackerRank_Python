

def average(array):
    # Convert list to sets to get rid of duplicates
    set_arr = set(array)

    # Calculate sum
    sum = 0
    myList = list(set_arr)
    for x in range(len(myList)):
        sum += myList[x]
    
    return  sum / len(myList)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)