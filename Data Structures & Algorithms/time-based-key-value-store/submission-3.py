class TimeMap:

    def __init__(self):
        # { "alice" : ("happy", 1), ("sad", 3), ("angry", 5) }
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.timeMap[key]

        l = 0
        r = len(lst) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if timestamp == lst[mid][1]:
                return lst[mid][0]
            elif timestamp > lst[mid][1]:
                res = lst[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res