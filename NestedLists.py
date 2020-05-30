# Sample Input
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output
# Berry
# Harry

def print_arr(arr):
    print(', '.join(str(x) for x in arr))



if __name__ == '__main__':
    myList = []
    for _ in range(int(input())):
        # global myList
        name = input()
        score = float(input())
        student = [name, score]
        myList.append(student)

    # Sort list by grade
    # Lambda - function can take any number of arguments, but can only have one expression.
    # lambda (args): (func) 
    sorted_arr = sorted(myList, key = lambda x: x[1])
    print_arr(sorted_arr)
    
    # Determine second to the lowest grade
    lowest = sorted_arr[0]
    i = 1
    while (lowest[1] == sorted_arr[i][1]):
       i += 1
    second_lowest = sorted_arr[i]
    print('Second Lowest:', second_lowest)
    
    # Determine every students with the second to lowest grade 
    # Sort by name
    seconds = []
    for student in sorted_arr:
        if (student[1] == second_lowest[1]): seconds.append(student[0])
    
    seconds = sorted(seconds)
    
    # Print the names
    for x in seconds: print(x)

    

    



    
