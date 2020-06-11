
# Sample Input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

# Sample Output
# 8

def findCaptainRoom(k, myList):

    # Get each distinct room using set
    my_Set = set(myList)

    # Determine room with only 1 occupant
    return ((sum(my_Set)*k)-(sum(myList))) // (k-1)



if __name__ == "__main__":

    k, myList = int(input()), list(map(int,input().split()))
    # k = 5
    # myList = [1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]

    print(findCaptainRoom(k, myList))

   
