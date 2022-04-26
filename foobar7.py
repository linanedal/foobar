class Graph:

    def __init__(self, vertices):
        self.n = vertices # n = number of vertices
        self.graph = []

    def create_edge(self, a, b, weight):
        # add an edge between a and b to the graph
        self.graph.append([a, b, weight])

    def BellmanFord(self, start):

        # start: 0
        # end: n-1
        n = self.n # number of vertices

        # initialize distance to each vertex to infinity
        distance = [float('inf')] * n
        distance[start] = 0 # start to itself is 0

        # relax edges n-1 times
        for _ in range(n-1):
            for a, b, weight in self.graph:
                if distance[a] + weight < distance[b]:
                    distance[b] = distance[a] + weight

        to_vertex = []
        for endpoint in range(n):
            to_vertex.append(distance[endpoint])
        return to_vertex

    def completepairs(self):

        allpairs = []
        for source in range(self.n): # with each vertex as the source
            allpairs.append(self.BellmanFord(source))

        return allpairs

    def checkneg(self, matrix):

        d_from_source = matrix[0]
        n = len(matrix)

        for a in range(n):
            for b in range(n):
                weight = matrix[a][b]
                if d_from_source[a] + weight < d_from_source[b]:
                    return True
        return False


def pathcost(distances, bunnies):

    n = len(distances)

    cost = 0 # initialize
    for b in range(len(bunnies) - 1):
        current = bunnies[b]
        next = bunnies[b + 1]
        cost += distances[current][next]
    start = 0
    end = n - 1

    cost += distances[start][bunnies[0]] # first bunny
    cost += distances[bunnies[-1]][end] # last bunny

    return cost


def permute(bunny_id, n):

    import itertools as it
    gen = it.permutations(bunny_id, n)
    return gen


def solution(times, time_limit):
    # Your code here
    n = len(times) # n = # of vertices
    creategraph = Graph(n)

    # create edges in the graph
    for row in range(n):
        for col in range(n):
            a, b, weight = row, col, times[row][col]
            creategraph.create_edge(a, b, weight)

    allpairs = creategraph.completepairs()
    ifneg = creategraph.checkneg(allpairs)

    if ifneg == True: # if there is a neg cycle
        return range(n - 2) # n-2 is the number of bunnies

    bunny_num = [b+1 for b in range(n-2)]

    for width in range(n-2, 0, -1):
        for permutation in permute(bunny_num, width):
            # print("width: ", width)
            # print("permutation: ", permutation, "\n")
            cost = pathcost(allpairs, permutation)
            if cost <= time_limit:
                ans = [b - 1 for b in permutation]
                ans.sort()
                return ans

    return []


times = [[0, 2, 2, 2, -1],
        [9, 0, 2, 2, -1],
        [9, 3, 0, 2, -1],
        [9, 3, 2, 0, -1],
        [9, 3, 2, 2, 0]]

times2 = [[0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0]]

solution(times2, 3)

solution(times, 1)
