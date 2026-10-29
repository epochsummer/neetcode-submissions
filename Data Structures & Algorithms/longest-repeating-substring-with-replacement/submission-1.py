class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}
        left: int = 0
        maximum = 0
        for right in range(len(s)):
            dictionary[s[right]] = dictionary.get(s[right],0) + 1 
            if (int(right)-left + 1) - max(dictionary.values()) > k:
                dictionary[s[left]] -= 1
                left += 1
            maximum = max(maximum,right-left+1)

        return maximum



        