class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret=[]
        for i in range(len(nums)) :
            if target-nums[i] in nums and i!=nums.index(target-nums[i]): 
                ret.append(nums.index(target-nums[i]))
                ret.append(i)
                break
        return ret
