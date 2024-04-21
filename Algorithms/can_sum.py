class CanSum:
    def canSum(self, target_sum, numbers):
        if target_sum == 0:
            return True
        if target_sum < 0:
            return True

        for num in numbers:
            remainder = target_sum - num
            if self.canSum(remainder, numbers) == True:
                return True

        return False

    def can_sum(self, target_sum, numbers, memo={}):
        if target_sum in memo:
            return memo[target_sum]
        if target_sum == 0:
            return True
        if target_sum < 0:
            return False
        for num in numbers:
            remainder = target_sum-num
            if self.can_sum(remainder, numbers, memo) == True:
                memo[target_sum] = True
                return True
        memo[target_sum] = False
        return False


cs = CanSum()
print(cs.can_sum(7, [2, 3]))
print(cs.can_sum(7, [5, 3, 4, 7]))
print(cs.can_sum(7, [2, 4]))
print(cs.can_sum(7, [2, 3, 5]))
print(cs.can_sum(300, [7, 14]))
