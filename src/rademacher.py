from itertools import combinations, product


class h:
    def __init__(self, intervals):
        self.intervals = intervals

    def predict(self, x):
        for (s, e) in self.intervals:
            if s <= x and x <= e:
                return 1

        return -1


class H:
    all_h = []

    def __init__(self, K, m):
        self.m = m
        points = list(range(m + K))

        for starting_points in combinations(points, K):
            partitions = [points[i: j] for i, j in zip(
                starting_points, starting_points[1:] + tuple([None]))]

            for ending_points in list(product(*partitions)):
                self.all_h.append(
                    h(tuple(zip(starting_points, ending_points))))

    def rademacher(self):
        rm = 0
        outputs = {-1, 1}

        for sigma in product(outputs, repeat=self.m):
            max_score = float('-inf')

            for h in self.all_h:
                score = 0

                for i in range(self.m):
                    score += sigma[i] * h.predict(i)

                if score > max_score:
                    max_score = score

            rm += max_score

        return rm / (2**self.m * self.m)


for m in range(1, 21):
    h_space = H(3, m)
    print("rademacher complexity of m = {} is {}".format(m, h_space.rademacher()))