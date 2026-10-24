class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        lst = []
        for i in strs:
            length = len(i)
            lst.append(str(length) + "#" + i)
        return "".join(lst)

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
                j = i
                while s[i] != "#":
                    i+=1
                length = int(s[j:i])
                word = s[i+1:i+1+length]
                i = i + length + 1
                lst.append(word)
        return lst


            