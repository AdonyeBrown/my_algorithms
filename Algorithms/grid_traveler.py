class GridTraveler:
    def grid_traveler_memo(self, m, n, memo={}):
        if (m, n) not in memo:
            if m == 1 and n == 1:
                return 1
            elif m == 0 or n == 0:
                return 0
            else:
                memo[m, n] = self.grid_traveler_memo(m-1, n, memo) + \
                    self.grid_traveler_memo(m, n-1, memo)

        return memo[m, n]


def main():
    gt = GridTraveler()
    print(gt.grid_traveler_memo(1, 1))
    print(gt.grid_traveler_memo(2, 3))
    print(gt.grid_traveler_memo(3, 2))
    print(gt.grid_traveler_memo(3, 3))
    print(gt.grid_traveler_memo(18, 18))
    print(gt.grid_traveler_memo(20, 20))


main()
