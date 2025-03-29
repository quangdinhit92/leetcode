class SmallestInfiniteSet(object):

    def __init__(self):
        self.removed = []
        self.setRemoved = set()
        self.currentSmallest = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.removed:

            smallest = heapq.heappop(self.removed)
            self.setRemoved.remove(smallest)

            return smallest
        else:
            self.currentSmallest += 1
            return self.currentSmallest - 1

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.currentSmallest and num not in self.setRemoved:
            self.setRemoved.add(num)
            heapq.heappush(self.removed, num)
            self.setRemoved.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
