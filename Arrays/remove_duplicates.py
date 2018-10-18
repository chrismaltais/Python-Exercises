class Solution:
    def remove_duplicates(self, nums):
        unique_numbers = 0
        for i in range(1, len(nums)):
            if (nums[i] != nums[unique_numbers]):
                unique_numbers += 1
                nums[unique_numbers] = nums[i]
        return unique_numbers +1 #bc started at 0