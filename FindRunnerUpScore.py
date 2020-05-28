

def prompt_user():
    user_input = []
    print('Enter number of elements: ')
    n = int(input())
    print('Enter {} elements: '.format(n))
    myList = map(int, input().split())
    user_input.append(n)
    user_input.append(myList)
    return user_input

def getRunnerUp(arr):
    sortedArr = sorted(arr)
    maxNum = sortedArr[len(sortedArr) - 1]
    i = 2
    while (maxNum == sortedArr[len(sortedArr) - i]):
        i += 1
    runnerUp = sortedArr[len(sortedArr) - i]

    print_arr(sortedArr)
    print('Runner Up:', runnerUp)

def print_arr(arr):
    print(', '.join(str(x) for x in arr))


if __name__ == '__main__':

    # Map(func, iter) - executes function for each item in a iterable
    # Wraps every element as an int
    # arr = map(int, input().split())

    # Prompt user for the values needed
    arr = prompt_user()

    # Get runner up algorithm
    getRunnerUp(arr[1])



