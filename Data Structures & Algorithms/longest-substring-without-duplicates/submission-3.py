class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0

        alphabets = set()

        for right in range(len(s)):
            while s[right] in alphabets:
                alphabets.remove(s[left])
                left += 1
                
            alphabets.add(s[right])
            longest = max(longest,right-left+1)
        return longest
            
       
        