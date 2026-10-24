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
            if s[i].isdigit():
                j = i
                while s[j] != "#":
                    j+=1
                length = int(s[i:j])
                i = j+1+length
                word = s[j+1:i]
                lst.append(word)
        return lst


            