from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    final = []
    for i in nested_arr:
        if len(i) == 1:
            final.extend(i)
        else:
            j = 0
            while j != len(i)-1:
                maximum = max(i[j],i[j+1])
                j+=1

            final.append(maximum)

    return final


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
