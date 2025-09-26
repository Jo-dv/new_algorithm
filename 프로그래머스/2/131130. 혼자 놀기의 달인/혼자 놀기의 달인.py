def solution(cards):
    answer = 0
    check = [False] * (len(cards) + 1)
    cards = [-1] + cards
    group = []
    box = []
    pos = 1
    
    while True:
        if check[pos]:
            group.append(len(box))
            box = []
            for i in range(1, len(cards)):
                if not check[i]:
                    pos = i
                    break
            else:
                break
        check[pos] = True
        box.append(cards[pos])
        pos = cards[pos]
    
    if len(group) >= 2:
        group.sort(reverse=True)
        return group[0] * group[1]
    
    return 0