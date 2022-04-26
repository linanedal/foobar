import numpy as np

def isPath(mat):

    # establish rows and columns
    row = len(np.array(mat))
    col = len(np.array(mat)[0])

    mat = np.matrix(mat)
    verify = mat.copy()

    verify[(row-1), (col-1)] = 1
    lastval = 1

    adjacents = [1]
    while len(adjacents) != 0:
        indices = np.where(verify == lastval)
        # what are their coordinates?
        coords = list(zip(indices[0], indices[1]))
        # check the adjacents:
        adjacents = []
        for cord in coords:
            check = get_adjacent_indices(cord[0], cord[1], row, col)
            zeros = [i for i in check if verify[i[0], i[1]] == 0]
            if len(zeros) != 0:
                [adjacents.append(i) for i in zeros]

        remove = []
        # if the one of the adjacents is not a 0,
        # put it in a list of items to be removed
        for t in adjacents: # for tuple in adjacents
            if verify[t] != 0:
                remove.append(t)
        for r in remove: # remove her
            adjacents.remove(r)

        if len(adjacents) == 0:
            break

        lastval += 1
        for c in adjacents:
            verify[c] = lastval

    if verify[0,0] == 0:
        return "There is no path."
    else:
        return verify

def get_adjacent_indices(i, j, m, n):
   adjacent_indices = []
   if i > 0:
       adjacent_indices.append((i-1,j))
   if i+1 < m:
       adjacent_indices.append((i+1,j))
   if j > 0:
       adjacent_indices.append((i,j-1))
   if j+1 < n:
       adjacent_indices.append((i,j+1))
   return adjacent_indices

def fill(mat):

    row = len(np.array(mat))
    col = len(np.array(mat)[0])

    filled = mat.copy()

    filled[(row-1), (col-1)] = 1 # fill exit

    lastval = 1
    while filled[0,0] == 0:
        # where are the cells that were last filled?
        indices = np.where(filled == lastval)
        # what are their coordinates?
        coords = list(zip(indices[0], indices[1]))
        # check the adjacents:
        adjacents = []
        for cord in coords:
            check = get_adjacent_indices(cord[0], cord[1], row, col)
            [adjacents.append(i) for i in check if i not in adjacents]

        remove = []
        # if the one of the adjacents is not a 0,
        # put it in a list of items to be removed
        for t in adjacents: # for tuple in adjacents
            if filled[t] != 0:
                remove.append(t)
        for r in remove: # remove her
            adjacents.remove(r)

        lastval += 1
        for c in adjacents:
            filled[c] = lastval

    return filled

def removex(mat):

    row = len(np.array(mat))
    col = len(np.array(mat)[0])

    # where are the -1 cells?
    indices = np.where(mat == -1)
    # what are their coordinates?
    coords = list(zip(indices[0], indices[1]))

    # what are their adjacents?
    toreplace = []
    for cord in coords:
        check = get_adjacent_indices(cord[0], cord[1], row, col)
        # do they have adjacents that are 0s?
        zeros = [i for i in check if mat[i[0], i[1]] == 0]
        if len(zeros) > 1:
            toreplace.append(cord)

    entranceval = []
    for cord in toreplace:
        mat[cord[0], cord[1]] = 0
        if isinstance(isPath(mat), np.matrix) == True:
            filler = mat.copy()
            filler = fill(filler)
            entranceval.append(filler[0,0])
            filler = np.zeros((row, col))
        mat[cord[0], cord[1]] = -1

    shortestpath = min(entranceval)

    return shortestpath

def solution(arr):
    # identify rows and columns
    row = len(arr)
    col = len(arr[0])
    # create matrix
    mat = np.matrix(arr)
    # replace all walls with a -1
    mat = np.where(mat == 0, 0, -1)

    shortestpath = removex(mat)

    return str(shortestpath)



# test1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# np.matrix(test1)
# test2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
#
# solution(test1)
#
#
#
# test4 = [[0, -1, 0, 0],[0,-1,0,-1],[-1,-1,0,0],[-1,-1,0,0]]
# test4mat = np.matrix(test4)
# test4mat
# isPath(test4mat)
#
#
# solution(test2)
