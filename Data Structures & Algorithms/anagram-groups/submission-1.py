class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortVisit = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in sortVisit:
                sortVisit[key] = []
            sortVisit[key].append(word)

        return list(sortVisit.values())