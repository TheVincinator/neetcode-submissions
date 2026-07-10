class CountSquares:

    def __init__(self):
        self.pointsFreq = defaultdict(int)
        self.pointsList = []

    def add(self, point: List[int]) -> None:
        self.pointsFreq[tuple(point)] += 1
        self.pointsList.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for (x, y) in self.pointsList:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            if (x, py) and (px, y) in self.pointsFreq:
                res += self.pointsFreq[(x, py)] * self.pointsFreq[(px, y)]
        return res
