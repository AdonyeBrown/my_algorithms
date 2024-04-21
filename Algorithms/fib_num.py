class FibNumMemo:
    def fib_num(self, n, memo={}):
        if n not in memo:
            if n <= 1:
                memo[n] = n
                return memo[n]
            else:
                memo[n] = self.fib_num(n-1, memo) + self.fib_num(n-2, memo)
        return memo[n]


def main():
    n = 100
    fib = FibNumMemo()
    print(fib.fib_num(n))


main()
