class UnionFind:
    def __init__(self, data):
        self.data = data

    def find(self, a):
        while self.data[a] != -1:
            a = self.data[a]

        return a

    def union(self, a, b):
        sentinel_a, sentinel_b = self.find(a), self.find(b)
        self.data[sentinel_a] = sentinel_b


if __name__ == "__main__":
    data = [-1 for x in range(10)]
    uf = UnionFind(data)
    print(data)
    print("find 1 before union with 2:", uf.find(1))
    uf.union(1,2)
    print(data)
    print("find 1 after union with 2:", uf.find(1))
    