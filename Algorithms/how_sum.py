class HowSum:
    def how_sum_1(self, target_sum, numbers):
        if target_sum == 0:
            return []  # return an empty list instead of assigning it to res
        if target_sum < 0:
            return None
        for num in numbers:
            remainder = target_sum - num
            remResult = self.how_sum_1(remainder, numbers)
            if remResult is not None:
                # return a list with num and the result of the recursive call
                return [num] + remResult
        return None

    def how_sum_2(self, target_sum, numbers, memo=None):
        # initialize the memo dictionary if it is None
        if memo is None:
            memo = {}
        # check if the target_sum is already in the memo
        if target_sum in memo:
            return memo[target_sum]
        # base cases
        if target_sum == 0:
            return []
        if target_sum < 0:
            return None
        # loop through the numbers
        for num in numbers:
            remainder = target_sum - num
            # recursively call the function with the remainder and the memo
            remResult = self.how_sum_2(remainder, numbers, memo)
            # if the recursive call returns a valid list, append the current num and store it in the memo
            if remResult is not None:
                memo[target_sum] = [num] + remResult
                return memo[target_sum]
        # if none of the numbers can sum up to the target, store None in the memo and return it
        memo[target_sum] = None
        return None


hs = HowSum()
print(hs.how_sum_2(7, [2, 3]))
print(hs.how_sum_2(7, [5, 3, 4, 7]))
print(hs.how_sum_2(7, [2, 4]))
print(hs.how_sum_2(8, [2, 3, 5]))
print(hs.how_sum_2(300, [7, 14]))
