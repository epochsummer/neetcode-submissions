class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for __ in range(9)]
        columns = [set() for __ in range(9)]
        boxes = [set() for __ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if  value != ".":

                    box_coord = (i // 3) * 3 + (j // 3)

                    if (value in rows[i] or
                        value in columns[j] or
                        value in boxes[box_coord]):
                        return False

                    rows[i].add(value)
                    columns[j].add(value) 
                    boxes[box_coord].add(value)


        return True  