class Twitter:

    def __init__(self):        
        self.tweets = defaultdict(list)## creates a new list for key not present in the list
        self.following = defaultdict(list)## following[user] : ## [list of users followed by user]
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time,tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for i in self.following[userId]:
            for t in self.tweets[i]:
                heapq.heappush(heap, t)
        for t in self.tweets[userId]:
            heapq.heappush(heap, t)
        
        res = []
        if len(heap) < 10:
            while len(heap) != 0:
                res.append(heapq.heappop(heap)[1])
            return res
        else:
            for i in range(10):
                res.append(heapq.heappop(heap)[1])
            return res

                

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            return None
        self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            return None
        self.following[followerId].remove(followeeId)
        
