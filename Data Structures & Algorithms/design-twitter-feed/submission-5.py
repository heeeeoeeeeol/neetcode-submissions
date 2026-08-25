class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets: self.tweets[userId] = [] 
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = self.tweets[userId].copy() if userId in self.tweets else []
        if userId in self.following: 
            for f in self.following[userId]: heap += self.tweets[f]
        return [x[1] for x in heapq.nlargest(10, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following: self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
