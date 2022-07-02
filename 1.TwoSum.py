class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        if len(nums) <0:
            return
        leng=len(nums)
        for n in range(0,leng): 
            for m in range(n+1,leng):
                if nums[n]+nums[m] ==target:
                    l.append(n) 
                    l.append(m)
                    return l
        
