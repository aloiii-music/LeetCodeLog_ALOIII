from collections import defaultdict 
class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        holder = defaultdict(int)
        for i in nums: 
            holder[i] +=1
        for i in holder:
            if holder[i] ==1:
                return i