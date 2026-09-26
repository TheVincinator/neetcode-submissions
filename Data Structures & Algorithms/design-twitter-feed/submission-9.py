class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        for time, tweetId in self.posts[userId]:
            heapq.heappush(minHeap, (time, tweetId))
            if len(minHeap) > 10:
                heapq.heappop(minHeap)
        for followeeId in self.following[userId]:
            for time, tweetId in self.posts[followeeId]:
                heapq.heappush(minHeap, (time, tweetId))
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)

        res = []
        for _ in range(len(minHeap)):
            res.append(heapq.heappop(minHeap)[1])

        res.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
