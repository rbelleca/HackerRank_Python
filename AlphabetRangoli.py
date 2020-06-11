# Sample Input: 5
# Sample Output:
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# Sample Input: 4
# ------d------
# ----d-c-d----
# --d-c-b-c-d--
# d-c-b-a-b-c-d
# --d-c-b-c-d--
# ----d-c-d----
# ------d------




def print_rangoli(size):
    # If size = 5, dashes = 4
    letter_size = (size)+(size-1)
    space_size = letter_size + (letter_size-1)
    total_size = letter_size + space_size
   
    # a = 97

    # Top Side
    for i in range(size):
        for j in in (total_size):
            str.rjust() 
    



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)