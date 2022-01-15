def solution(lottos, win_nums):
    zero   = lottos.count(0) # 0의 개수 확인
    result = len(list(set(lottos).intersection(win_nums))) # 당첨 번호의 개수 확인
    return rank(zero+result), rank(result)

def rank(result):
    if result == 6:
        return 1
    elif result == 5:
        return 2
    elif result == 4:
        return 3
    elif result == 3:
        return 4
    elif result == 2:
        return 5
    else:
        return 6    