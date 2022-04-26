def solution(l):

    import itertools as it
    # l is a list
    # eg. solution([3, 1, 4, 1])

    def list_to_str(list):
        string = str()
        for l in list:
            lstr = str(l)
            string += lstr
        return string

    def tup_to_int(tuple):
        string = str()
        for t in tuple:
            string += t
        integer = int(string)
        return integer

    def permute(string, length):
        perms = it.permutations(string, length)
        permlist = []
        for tup in perms:
            permint = tup_to_int(tup)
            permlist.append(permint)
        return permlist

    def by3(num):
        if num % 3 == 0:
            return True
        else:
            return False


    length = len(l)
    stringl = list_to_str(l)

    toptrues = []
    for n in range(1, length+1):
        nperms = permute(stringl, n)
        true3 = [i for i in nperms if by3(i)==True]
        if len(true3)==0:
            toptrues.append(0)
        else:
            toptrues.append(max(true3))


    return max(toptrues)


solution([3, 1, 4, 1])
solution([3, 1, 4, 1, 5, 9])
