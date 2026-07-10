class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y) in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            if (x, py) in self.points and (px, y) in self.points:
                res += self.points[(x, y)] * self.points[(x, py)] * self.points[(px, y)]
        return res
