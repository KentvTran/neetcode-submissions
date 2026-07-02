class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        visited = {}

        for char in s:
            visited[char] = visited.get(char,0) + 1

        for char in t:
            visited[char] = visited.get(char,0) - 1

        for value in visited.values():
            if value != 0:
                return False
        
        return True

        
