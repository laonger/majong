#!/usr/bin/python
# encoding: utf-8

def shun(*cards):
    """# peng: 顺 """
    a = -1
    for i in cards:
        if a == -1:
            a = i[1]
            continue
        if i[1] != a+1:
            return False
        a = i[1]
    return True

def xiangtong(*cards):
    """# xiangtong: N个牌相同 """
    return bool([i for i in cards if i != cards[0]])

def majong(*cards):
    """# majong: 麻将牌
    """
    return len(cards) == 2 and xiangtong(*cards)

def peng(*cards):
    """# peng: 碰 """
    return len(cards) == 3 and xiangtong(*cards)

def gang(*cards):
    """# gang: 杠
    """
    return len(cards) == 4 and xiangtong(*cards)
    

def tongse(*cards):
    """# tongse: 同色 """
    return bool([i[0] for i in cards if i[0] != cards[0][0]])

    
    
    
    
