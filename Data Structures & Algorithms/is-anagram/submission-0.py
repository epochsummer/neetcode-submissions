class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        for i in s:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        
        for i in t:
            if i not in dictionary:
                return False
            else:
                dictionary[i] -= 1
        
        for values in dictionary.values():
            if values !=0:
                return False
        
        return True
        