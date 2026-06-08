class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # {"alice" : [("happy", 1), ("sad", 3)]}
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.timeMap[key]
        if lst == [] or lst[0][1] > timestamp:
            return ""
        l = 0
        r = len(lst) - 1
        i = l
        while l <= r:
            mid = (l + r) // 2
            if lst[mid][1] < timestamp:
                i = mid
                l = mid + 1
            elif lst[mid][1] > timestamp:
                r = mid - 1
            else:
                return lst[mid][0]
        return lst[i][0]