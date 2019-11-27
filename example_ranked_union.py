class UnionFind:
    def __init__(self, data):
        self.data = data
        self.ranks = [0 for n in data]

    def find(self, a):
        while self.data[a] != -1:
            a = self.data[a]

        return a

    def union(self, a, b):
        sentinel_a, sentinel_b = self.find(a), self.find(b)
        if self.ranks[sentinel_a] < self.ranks[sentinel_b]:
            self.data[sentinel_a] = sentinel_b
        elif self.ranks[sentinel_a] == self.ranks[sentinel_b]:
            self.data[sentinel_a] = sentinel_b
            self.ranks[sentinel_b] += 1
        else:
            self.data[sentinel_b] = sentinel_a


if __name__ == "__main__":
    data = [-1 for n in range(10)]
    uf = UnionFind(data)
    print("union of equal rank sets")
    print("data and ranks before union:", data, uf.ranks)
    uf.union(1,8)
    print("data and ranks after union: ", data, "", uf.ranks)
    
    print("union of unequal rank sets")
    print("data and ranks before union:", data, uf.ranks)
    uf.union(1,5)
    print("data and ranks after union: ", data, "", uf.ranks)
    