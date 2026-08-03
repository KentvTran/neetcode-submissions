class MedianFinder:

    def __init__(self):
        #python heapq is min heap by default
        #to stimulate max-heap for smaller half of numbers we will multiply all numbers pushed here by -1
        self.small = []

        #still standard min-heap for larger half of numbers
        self.large = []

    def addNum(self, num: int) -> None:
        #if large heap has item and new number is bigger than smallest number in large half
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else: #otherwise push to small half(multiply by -1 to keep largest number at the top)
            heapq.heappush(self.small, -1 * num)

        #if the small heap grown too big
        if len(self.small) > len(self.large) + 1:
            #pop max number from small
            val = -1 * heapq.heappop(self.small)
            #push to large 
            heapq.heappush(self.large, val)
        #if large grown too large
        if len(self.large) > len(self.small) + 1:
            #pop min number from large
            val = heapq.heappop(self.large)
            #push to small
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        #if small has more elements then median is small top element
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        #if large has more elements than median is its top element
        elif len(self.large) > len(self.small):
            return self.large[0]
        #if they are same size than find mean of two 
        return (-1 * self.small[0] + self.large[0]) / 2.0
        
        