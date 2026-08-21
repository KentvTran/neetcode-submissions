class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #build graph
        adjMap = {i:[] for i in range(n)}
        for fromI, toI, price in flights:
            adjMap[fromI].append([toI,price])

        #minimum tracker
        prices = [float("inf")]*n
        prices[src] = 0

        #bfs ques stores: current node, current toal, stops taken
        queue = collections.deque([(src, 0, 0)])

        #bfs
        while queue:
            node, cost, stops = queue.popleft()

            #prune
            if stops > k:
                continue
            for neighNode, neighPrice in adjMap[node]:
                nextCost = cost + neighPrice

                #prune
                if nextCost < prices[neighNode]:
                    prices[neighNode] = nextCost
                    queue.append((neighNode, nextCost, stops + 1))
        return prices[dst] if prices[dst] != float("inf") else -1