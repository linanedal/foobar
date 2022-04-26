def solution(xs):
    # xs is a list of integers
    import itertools as it
    import numpy as np
    from operator import mul
    from functools import reduce

    # count integer types
    def countpos(list):
        return len([i for i in list if i>0])
    def count0(list):
        return len([i for i in list if i==0])
    def countneg(list):
        return len([i for i in list if i<0])

    # make count string
    def list_to_str(list):
        string = str()
        for l in list:
            lstr = str(int(l))
            string += lstr
        return string

    # check type of nums in xs and return method
    # negs: 0,3,4,5
    #   only neg: 3,4
    def checkmethod(counts):
        options = ['111','110','100','001','011','101','010']
        for o in range(len(options)):
            if counts == options[o]:
                return o

    def discard0(list): # returns nonzero values
        return [i for i in list if i!=0]

    def checknegs(list): # checks # of negatives
        negnum = len([i for i in list if i<0])
        return "Even" if negnum % 2 == 0 else "Odd"

    def lowestabs(list): # id's the lowest absolute value, returns minimum
        abslist = [abs(i) for i in list]
        minimum = min(abslist)
        return minimum

    def product(list):
        return reduce(mul, list)

    length = len(xs)


    counts = [countpos(xs), count0(xs), countneg(xs)]
    for i in range(3):
        if counts[i] != 0:
            counts[i] /= counts[i]
    counts = list_to_str(counts)
    method = checkmethod(counts)

    # if xs has 0s in it
    if method == 0 or method == 1 or method == 4 or method == 6:
        if method != 6: # if there's something other than 0s
            xs = discard0(xs)
        else: # if there's only 0s
            sol = 0
    # if xs has negatives
    if method == 0 or method == 3 or method == 4 or method == 5:
        negnum = checknegs(xs)
        if negnum == "Odd":
            if length != 1:
                num = lowestabs([i for i in xs if i<0])
                xs.remove(-num)
            else:
                sol = xs[0]

    if all(n == 0 for n in xs): # if after removing smallestneg, list is all 0s
        sol = 0
    else:
        sol = product(xs)

    return str(sol)


solution([999,999,999,999,999,999,999,999,999])
solution([2, 0, 2, 2, 0])
solution([-2, -3, 4, -5])

solution([2,-100])
solution([2,0,0,-100])

solution([-99, 0, 99])
solution([-50,-2,-90,0,-2,-2,-2])
solution([0])
solution([3,4,5,6])
solution([4,5,6])
#
#
godforsakenlist = [999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999]
solution(godforsakenlist)
