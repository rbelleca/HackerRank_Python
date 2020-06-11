# Capitalize

def solve(s):
    # myList = s.split()
    # newStr = ''
    # for s in myList:
    #     if (s.isdigit()): 
    #         # print(f'{s} has a digit!')
    #         newStr += s 
    #     else:
    #         # print(f'{s} has no digit!')
    #         newStr += s.capitalize() 
    #     newStr += ' '
    
    # # print(newStr)
    # return newStr

    # or

    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
   
if __name__ == "__main__":
    s = input()
    solve(s)