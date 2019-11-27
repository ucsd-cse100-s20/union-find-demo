class UnionFind:
    def __init__(self, data):
        self.data = data

    def find(self, a):
        path = []
        while self.data[a] != -1:
            path.append(a)
            a = self.data[a]

        self.__compress_path(path, a)
        
        return a

    def __compress_path(self, path, sentinel):
        for x in path:
            data[x] = sentinel


    def union(self, a, b):
        sentinel_a, sentinel_b = self.find(a), self.find(b)
        self.data[sentinel_a] = sentinel_b


if __name__ == "__main__":
    data = [-1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
    uf = UnionFind(data)
    print("data before path compression:", data)
    uf.find(1)
    print("data after path compression: ", data)
    