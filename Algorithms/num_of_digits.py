import math


class NumDigit:
    def func(self, n: int) -> int:
        """
        This function counts the number os digits in a number
        It takes O(n) times to execute
        """
        # Intialize a variable to zero
        res = 0
        while n > 0:
            n = n//10
            res += 1
        return res

    def fun(self, n: int) -> int:
        """
        This function counts the number os digits in a number
        It takes O(1) times to execute
        """
        return math.floor(math.log10(n) + 1)


count_number_of_digits = NumDigit()
print(count_number_of_digits.func(7894))
print(count_number_of_digits.fun(7894))
