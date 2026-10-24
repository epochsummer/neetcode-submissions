class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for i in s:
            if i == "(" or i =="{" or i =="[":
                lst.append(i)
            else:
                if len(lst) == 0:
                    return False
                if i == "}":
                    if lst[-1] != "{":
                        return False
                    else:
                        lst.pop()
                elif i == "]":
                    if lst[-1] != "[":
                        return False
                    else:
                        lst.pop()
                else:
                    if lst[-1] != "(":
                        return False
                    else:
                        lst.pop()
        if len(lst) != 0:
            return False
        return True