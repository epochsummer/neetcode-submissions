class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        first = 0
        last = len(s) - 1

        while first < last:
            if not (97<ord(s[first])<122 or s[first].isalnum()):
                first += 1

            elif not (97<ord(s[last])<122 or s[last].isalnum()):
                last-=1

            else:
                if s[first] != s[last]:
                    return False
                first += 1
                last -= 1

        return True
        