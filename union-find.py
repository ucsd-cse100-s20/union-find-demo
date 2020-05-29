class UnionFind:
    def __init__(self, data):
        self.data = data
        self.ranks = [0 for n in data]

    def find(self, a):
        path = []
        while(self.data[a] != -1):
            path.append(a)
            a = self.data[a]

        self.__path_compression(path, a)

        return a

    def __path_compression(self, path, sentinel):
        for x in path:
            self.data[x] = sentinel

    def union(self, a, b):
        sentinel_a, sentinel_b = self.find(a), self.find(b)
        if self.ranks[sentinel_a] < self.ranks[sentinel_b]:
            self.data[sentinel_a] = sentinel_b
        else:
            self.data[sentinel_b] = sentinel_a
            if self.ranks[sentinel_a] == self.ranks[sentinel_b]:
                self.ranks[sentinel_a] += 1


if __name__ == "__main__":
    data = [-1 for n in range(10)]
    uf = UnionFind(data)
    print(uf.data, uf.ranks)
    # union of equal ranks
    uf.union(1, 8)
    print(uf.data, uf.ranks)

    # union of unequal ranks
    uf.union(1, 5)
    print(uf.data, uf.ranks)
    

    # interview question:
    # given matrix of 0's and 1's where 0's are water and 1's are island
    # how many islands are there?

    # union find approach (not the only possible approach):
    # 1. put each 1 in their own set
    # 2. whenever you find two 1's neighboring eachother, call union on them
