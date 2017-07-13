#!/usr/bin/python
# encoding: utf-8

import copy
import random


import group_check

CARDS = {
    'T': {   # 筒
        1: ('T', 1),
        2: ('T', 2),
        3: ('T', 3),
        4: ('T', 4),
        5: ('T', 5),
        6: ('T', 6),
        7: ('T', 7),
        8: ('T', 8),
        9: ('T', 9),
    },
    'W': {    # 万
        1: ('W', 1),
        2: ('W', 2),
        3: ('W', 3),
        4: ('W', 4),
        5: ('W', 5),
        6: ('W', 6),
        7: ('W', 7),
        8: ('W', 8),
        9: ('W', 9),
    },
    'S': {    # 索
        1: ('S', 1),
        2: ('S', 2),
        3: ('S', 3),
        4: ('S', 4),
        5: ('S', 5),
        6: ('S', 6),
        7: ('S', 7),
        8: ('S', 8),
        9: ('S', 9),
    },
    'Z': {
        1: ('Z', 1),  # 中
        2: ('Z', 2),  # 发
        3: ('Z', 3),  # 白
    },
    'F': {
        1: ('F', 1),  # 东
        2: ('F', 2),  # 南
        3: ('F', 3),  # 西
        4: ('F', 4),  # 北
    }
}

ALL_CARDS = []
for i in '1234':
    for v in CARDS.itervalues():
        ALL_CARDS.extend(v.values())

"""
0 1 2 3 4 5 6 7 8 9 10 11 12 13
"""

RULES = {
    # 清一色
    'qingyise': [
        'Xa X(a+1) X(a+2) ; X1 X2 X3 X4 X5 X6 X7 X8 X9 ; Xa Xa',
    ],

    #一色三同顺
    'yisesantongshun': [
        'xa x(a+1) x(a+2) xa x(a+1) x(a+2) xa x(a+1) x(a+2) ; xa x(a+1) x(a+2) ; xa xa',
    ],
    # 七星不靠
    'qixingbukao': [
        'a[b,b+3,b+6]{2};F1 F2 F3 F4 Z1 Z2 Z3'
    ],
}


## qingyise
#tongse(*hand_cards) and (
#    shun(hand_cards[0], hand_cards[1], hand_cards[2]) 
#    and shun(*hand_cards[3:11]) 
#    and majong(hand_cards[12], hand_cards[13])
#)

great_wall = [
    [],
    [],
    [],
    [],
]

temp = ALL_CARDS[:]
for i in xrange(4):
    for _ in xrange(len(ALL_CARDS)/4):
        v = random.choice(temp)
        great_wall[i].append(v)
        temp.remove(v)
    
table_cards = []
    
USER = {
    'all': [],  # ('F', 1), ('F', 2)
    'hand': [], # num
    'chi': [],  # num
    'peng': [], # num
    'gang': [], # num
}

users = {
    1: copy.deepcopy(USER),
    2: copy.deepcopy(USER),
    3: copy.deepcopy(USER),
    4: copy.deepcopy(USER),
}

i = 0
ii = 0
for u in xrange(1, 5):
    for _ in xrange(13):
        c = great_wall[i][ii]
        ii =+1
        if ii == len(ALL_CARDS)/4 -1:
            ii = 0
            i +=1
        user[u]['all'].append(c)
    user[u]['hand'] = user[u]['all'][:]
