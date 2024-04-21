class Factorial:
    def factorial(self, n):
        if n <= 1:
            return 1
        else:
            return n * self.factorial(n-1)


def main():
    n = 6
    fact = Factorial()
    print(fact.factorial(n))


main()
