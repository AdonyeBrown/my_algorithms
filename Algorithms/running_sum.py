class RunningSum:
    def runningSum(self, nums):
        s = 0
        running_sum = []

        for num in nums:
            s += num
            running_sum.append(s)

        return running_sum


nums = [2, 7, 4, 6, 1, 5]
rs = RunningSum()
print(rs.runningSum(nums))
