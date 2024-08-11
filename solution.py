class Solution(object):
    def numOfPairs(self, nums, target):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    count += 1
        return count


solution = Solution()

nums1, target1 = ["777","7","77","77"], "7777"
nums2, target2 = ["123","4","12","34"], "1234"
nums3, target3 = ["1","1","1"], "11"

print(solution.numOfPairs(nums1, target1))  
print(solution.numOfPairs(nums2, target2))  
print(solution.numOfPairs(nums3, target3))  
