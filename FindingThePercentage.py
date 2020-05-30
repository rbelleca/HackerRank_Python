
def getAverage(myList):
    sum = 0
    for x in myList: 
        sum += x 
    return '%.2f' % round((sum / len(myList)), 2)

if __name__ == '__main__':
    # Prompt number of students
    n = int(input())

    
    student_marks = {}
    for _ in range(n):
        # Prompt student's name with 3 float values 
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    # Prompt which student to get average grade of
    query_name = input()

    # Find the query_name in the student_marks
    if query_name in student_marks:
        # Returns the value pair which is a list in this case
       grades = student_marks[query_name] 
       print(getAverage(grades))