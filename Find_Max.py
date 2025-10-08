class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return -1;
        maxElement=nums[0]
        maxIndex=0
        for i in range(1,n):
            if nums[i]>maxElement:
                maxElement=nums[i]
                maxIndex=i    
        return maxIndex