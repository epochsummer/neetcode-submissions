class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            lst = [0] * 26
            for letter in string:
                lst[ord(letter) - ord("a")] += 1

            if tuple(lst) not in dic: 
                value_lst = []
                value_lst.append(string)
                dic[tuple(lst)] = value_lst
            else:
                dic[tuple(lst)].append(string)
            

        final_ans = []
        for key in dic:
            final_ans.append(dic[key])
        
        return final_ans