# -*- coding: UTF-8 -*-
'''
Created on 2019年4月27日

@author: 13892
'''
import itertools

def verify(num):
    return ('float', 'int')[round(float(num)) == float(num)]
def x():
    num_lst = "123456789"
    oper_lst = "+-*/"
    num_groups = itertools.combinations(num_lst, 4)
    oper_groups = list(itertools.product(oper_lst, repeat=3))
    expressions_groups = ["{}{}{}{}{}{}{}",
        "({}{}{}){}{}{}{}","(({}{}{}){}{}){}{}",
        "{}{}({}{}{}){}{}","{}{}(({}{}{}){}{})","({}{}({}{}{})){}{}",
        "{}{}{}{}({}{}{})","{}{}({}{}({}{}{}))",
        "({}{}{}){}({}{}{})"
        ]
    res = {}
    for num_group in num_groups:
        seq_continue = []
        for num in itertools.permutations(num_group, 4):
            for oper_group in oper_groups:
                for expressions in expressions_groups:
                    try:
                        temp = eval(expressions.format(float(num[0]), oper_group[0], float(num[1]), oper_group[1], float(num[2]), oper_group[2], float(num[3])))
                        if temp > 0 and verify(temp) == "int":
                            seq_continue.append(temp)
                    except:
                        pass
        res["".join(num_group)] = len((max_seq(sorted(list(set(seq_continue))))))
        print(num_group,len((max_seq(sorted(list(set(seq_continue)))))))
    print(max(res.items(),key=lambda x:x[1]))
def max_seq(lst):
    seq = []
    for k, g in itertools.groupby(enumerate(lst), lambda x: x[1] - x[0]):
        seq.append([v for i, v in g])
    return max(seq,key=lambda x:len(x))

if __name__ == '__main__':
    x()
