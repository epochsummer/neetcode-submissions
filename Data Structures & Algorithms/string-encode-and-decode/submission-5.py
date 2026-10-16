class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = []
        for i in strs:
            length = len(i)
            string = str(length) + "#" + i
            temp.append(string)
        return "".join(temp)


    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        j = 0
        while i < len(s):
            if s[j] != "#":
                j+=1
            else:
                length = int(s[i:j])
                string = s[j+1:j+1+length]
                lst.append(string)
                i = j + length + 1
                j = i
        return lst



