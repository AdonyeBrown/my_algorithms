class TwoSum:
    def twoSum_1(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity O(n^2)-> exponential runtime
        space complexity O(1) constant space
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target-nums[i]:
                    return [i, j]

    def twoSum_2(self, nums: list[int], target: int) -> list[int]:
        """
        Two-pass hash table
        Time complexity O(n) -> linear runtime
        Space complexity O(n) -> linear space
        """
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map and map[complement] != i:
                return [i, map[complement]]

    def twoSum_3(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [i, map[complement]]
            map[nums[i]] = i


num = [2, 7, 3, 9]
target = 5
ts = TwoSum()
print(ts.twoSum_1(num, target))
print(ts.twoSum_2(num, target))
print(ts.twoSum_3(num, target))
