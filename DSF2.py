class DisjointSetForest:
    def __init__(self, n):
        self.forest = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index < len(self.forest)

    # Problem 6
    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.forest[a] < 0:
            return a

        return self.find(self.forest[a])

    # Problem 7
    def find_contains_loop(self, a, s=None):
        if not self.is_index_valid(a):
            return -1

        if s is None:
            s = set()

        if a in s:
            print("Loop found")
            return -1

        s.add(a)

        if self.forest[a] < 0:
            return a

        return self.find_contains_loop(self.forest[a], s)

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:  # Problems 3 and 4
            self.forest[rb] = ra

    # Problem 2
    def in_same_set(self, a, b):
        if not self.is_index_valid(a) or not self.is_index_valid(b):
            return False

        return self.find(a) == self.find(b)

    # Problem 5
    def num_sets(self):
        count = 0

        for k in self.forest:
            if k < 0:
                count += 1

        return count

    # Problem 9
    def is_equal(self, dsf):

        if len(self.forest) != len(dsf.forest):
            return False

        # Running time O(n^2). Can you do it in O(n)? (:
        for i in range(len(self.forest)):
            for j in range(len(self.forest)):
                if self.in_same_set(i, j) != dsf.in_same_set(i, j):
                    return False

        return True

    def __str__(self):
        return str(self.forest)


# Problem 8
def create_evens_odds_dsf(n):
    dsf = DisjointSetForest(n)

    for i in range(2, n):
        dsf.union(i, i % 2)

    return dsf


def main():
    dsf = DisjointSetForest(7)
    print(dsf)
    dsf.union(2, 3)
    print(dsf)
    dsf.union(0, 3)
    print(dsf)
    dsf.union(4, 5)
    print(dsf)
    dsf.union(3, 5)
    print(dsf)
    dsf.union(1, 4)
    print(dsf)


if __name__ == "__main__":
    main()
