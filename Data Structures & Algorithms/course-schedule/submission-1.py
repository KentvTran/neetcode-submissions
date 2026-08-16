class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build adj. list and populate with prereqs
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #tracks courses we are currently exploring
        visitSet = set() 

        def dfs(crs):
            if crs in visitSet: #cycle detected
                return False
            if preMap[crs] == []: #safe empty prereq list
                return True

            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs) #cleanup
            preMap[crs] = [] #mark safe

            return True
        
        #run dfs on every node -> incase graph is disconnected
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


        