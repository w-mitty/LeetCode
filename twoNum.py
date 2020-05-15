from typing import List

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for index_1 in range(len(nums)):
            for index_2 in range(index_1+1, len(nums)):
                if nums[index_1]+nums[index_2]==target:
                    return [index_1, index_2]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        num_dict = {};
        for i in range(len(nums)):
            if target-nums[i] in nums[:i]:
                return [num_dict[target-nums[i]], i]
            num_dict[nums[i]] = i #key collision

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        num_dict = {};
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in nums and num_dict[target-nums[i]]!=i:
                return [i, num_dict[target-nums[i]]]

if __name__ == '__main__':
    object = Solution()
    answer = object.twoSum2([3, 2, 4], 6)
    print(answer)