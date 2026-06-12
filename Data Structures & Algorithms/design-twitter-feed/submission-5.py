class Twitter:

    def __init__(self):
        self.tweets = defaultdict(set)
        # {1 : [(1, 10), (2, 20)], 2 : [(3, 30), (4, 40)]}
        self.following = defaultdict(set)
        # {1 : [2, 3], 2 : [1, 3], 3 : [2]}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].add((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        for time, tweetId in self.tweets[userId]:
            maxHeap.append((-time, tweetId))
        for followingId in self.following[userId]:
            if followingId == userId:
                continue
            for time, tweetId in self.tweets[followingId]:
                maxHeap.append((-time, tweetId))
        heapq.heapify(maxHeap)
        result = []
        for i in range(10):
            if maxHeap:
                result.append(heapq.heappop(maxHeap)[1])
            else:
                break
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
