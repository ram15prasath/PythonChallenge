class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums,start,end):
            while start<=end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1    
        k%=len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)