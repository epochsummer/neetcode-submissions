class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final_grade = 0
        lst = []
        for i in range(len(operations)):
            if operations[i] == "+":
                addition = int(lst[-1]) + int(lst[-2])
                lst.append(addition)
            elif operations[i] == "C":
                lst.pop()
            elif operations[i] == "D":
                multiply = int(lst[-1]) * 2
                lst.append(multiply)
            else:
                lst.append(operations[i])
        
        for i in lst:
            final_grade += int(i)
        
        return final_grade


        