class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) -1): # Getting the first number in array or next if we didn't get Target
            for j in range(i+1,len(nums)): # Getting the second number in array or next if we didn't get Target
                if nums[i] + nums[j] == target: # Comparing sum of numbers and if they are equel to target then wi will go to return but if not numbers will be changed
                    return(i, j) # returning the number of the location of the number in the array
        return[]