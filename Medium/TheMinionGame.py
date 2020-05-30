# Sample Input
# EQQAEAOQYEQEYYOEEQQYAOEEAQEEOOEYAYOEYAYAEOQYAAYAOYYOQAAYEQAOOAQ
# EAEYAOEEQYYEEAOAOAEQOEYOAOEYOOAAOQEOYEAYYOEAOAQEYYEOQEEEYAOOAYOO
# AQAEOYOYAEOYQEEEOOQOEAOAAQAOQEYOQEAEAEOOOOQOYQOEQQYEEEYEEOQYYYOEQ
# OQEYAYQQOYEEOAEQOEEEEAAEEYAAQAAQAAYOEAQAQYEYYYEAOYOQEQOOEQOYAYAEE
# YQAYYQYYAEAYOEYEAOQQQOYYYOYYOYYQYAOEOAOAOYEAAOEOEAEYQAEAQOEOYEEAQOA
# OQEYOEQOAQQEEYOOAQQOOEYQAQOEEOOOAAQOQEYYOEOOQOOAEYEOOAEQYQOAEYYYAQAYO
# EYOEYYEEOEEOAYAEEQEQOAAAYAEYQQAYOYQQOAEAOQOOYAEEOAEQAQEEQYOOEEAEEAAOY
# QYQAOEQYOYEQEAAOYAQAQYEAQEQEEOQQQYEYOQ

# Sample Ouput
# Kevin 82011

def minion_game(s):
    # Convert string to a list
    s_List = []
    for x in range(len(s)):
        s_List.append(s[x])

    def calculate_Stuart(s): 
        # Pair each consonant with every letters in string
        distinct_set = getDistinctWords_Con(s_List)
        
        # Count occurence of each distinct words
        wordScore_Dict = dict() 
        temp_list = list(distinct_set)
        for x in temp_list:
            count = countOccurence(s, x)
            wordScore_Dict.update({x:count})

        # Calculate points
        total_points = 0
        points_list = list(wordScore_Dict.values())
        for x in points_list:
            total_points += x

        return total_points
            
    def getDistinctWords_Con(s_List):
        temp_List = set()
        # Goes through each character of the string
        for i in range(len(s)):
            if (s_List[i] not in 'AEIOU'):
                # Goes through characters after
                for x in range(len(s)): 
                    if (s[i:x+1] == ''): continue
                    temp_List.add(s[i:x+1])

        return temp_List

    def getDistinctWords_Vow(s_List):
        temp_List = set()
        # Goes through each character of the string
        for i in range(len(s)):
            if (s_List[i] in 'AEIOU'):
                # Goes through characters after
                for x in range(len(s)): 
                    if (s[i:x+1] == ''): continue
                    temp_List.add(s[i:x+1])

        return temp_List

    def countOccurence(string, sub_string):
        count = 0
        for x in range(0, len(string)):
            if (string[x: x+len(sub_string)] == sub_string):
                count += 1
        return count

    def calculate_Kevin(s): 
        # Pair each consonant with every letters in string
        distinct_set = getDistinctWords_Vow(s_List)

        # Count occurence of each distinct words
        wordScore_Dict = dict() 
        temp_list = list(distinct_set)
        for x in temp_list:
            count = countOccurence(s, x)
            wordScore_Dict.update({x:count})
        
        # Calculate points
        total_points = 0
        points_list = list(wordScore_Dict.values())
        for x in points_list:
            total_points += x

        return total_points

    a = calculate_Stuart(s)
    b = calculate_Kevin(s)

    if a > b : print('Stuart', a)
    elif (b > a): print('Kevin', b)
    else: print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
   
    