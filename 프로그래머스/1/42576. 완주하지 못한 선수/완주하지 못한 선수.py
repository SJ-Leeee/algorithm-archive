def solution(participant, completion):
    pdict = {}
    
    for comp in completion: # 완주한 선수들 dict
        if comp in pdict: 
            pdict[comp] += 1
        else:
            pdict[comp] = 1
        
    for part in participant: # 참가자
        if part not in pdict or pdict[part] == 0:
            return part
        pdict[part] -= 1
    
    