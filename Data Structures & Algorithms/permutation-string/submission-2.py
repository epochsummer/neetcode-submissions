class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictionary = {}
        window = {}
        left = 0
    

        for alph in s1:
            dictionary[alph] = dictionary.get(alph,0) + 1

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right],0) + 1
            if right - left + 1 == len(s1):
                if window == dictionary:
                    return True
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
        return False




                



        