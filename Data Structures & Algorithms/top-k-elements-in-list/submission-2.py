
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        lst = [[] for __ in range(len(nums) + 1)]
        final = []


        # key: the number, value: how many it has
        for i in nums:
            dictionary[i] = dictionary.get(i,0) + 1

        for key,value in dictionary.items():
            lst[value].append(key)
        
        for i in range(len(lst) - 1,0,-1):
            final = final + lst[i]
            if len(final) == k:
                return final
        return final





        
        



        