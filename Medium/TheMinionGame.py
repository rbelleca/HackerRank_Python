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

# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(s):
    s_score = 0
    k_score = 0

    for i in range(len(s)):
        # Kevin gets points
        if s[i] in 'AEIOU':
            k_score += (len(s)-i)
        
         # Stuart gets points
        else:
            s_score += (len(s)-i)

    if s_score > k_score: print('Stuart', s_score)
    elif (k_score > s_score): print('Kevin', k_score)
    else: print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
    


