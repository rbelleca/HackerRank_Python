# Sample Input
# AABCAAADA
# 3

# Sample Output
# AB
# CA
# AD


def merge_the_tools(string, k):
    # Split string into segments with size k
    num_seg = len(string) / k
    list_seg = []
    for i in range(0, len(string), k):
        list_seg[i] = string[i:k]
    
    print(list_seg)
    # Determine distinct char; Eliminate duplicates
    
    # Print each segement
    

if __name__ == '__main__':
    # string, k = input(), int(input())
    # merge_the_tools(string, k)

    string = 'ABACAA'
    k = 3
    
     # Split string into segments with size k
    num_seg = len(string) / k
    list_seg = []
    for i in range(0, len(string), k):
        temp = ''
        for j in range(k):
            temp += string[j]
        list_seg[i] = temp
    print(list_seg)
    # Determine distinct char; Eliminate duplicates
    
    # Print each segement
