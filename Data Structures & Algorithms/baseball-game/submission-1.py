class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final_grade = 0
        lst = []
        for i in range(len(operations)):
            if operations[i] == "+":
                addition = lst[-1] + lst[-2]
                lst.append(addition)
            elif operations[i] == "C":
                lst.pop()
            elif operations[i] == "D":
                multiply = lst[-1] * 2
                lst.append(multiply)
            else:
                lst.append(int(operations[i]))
        
        for i in lst:
            final_grade += int(i)
        
        return final_grade


        