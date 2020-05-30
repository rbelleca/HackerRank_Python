

if __name__ == "__main__":
    
    # Prompt user input
    n1, a_list = input(), input().split()
    n2, b_list = input(), input().split()

    # Use set to get symmetric difference
    sym_set= set(a_list).difference(set(b_list))
    sym_set.update(set(b_list).difference(set(a_list)))

    # Convert set to list then sort
    sys_list = sorted(map(int, list(sym_set)))
    
    # Print result
    for x in sys_list:
        print(x)


    

