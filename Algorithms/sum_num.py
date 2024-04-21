def sum_num(n):
    # base case
    if n == 0:
        return 0
    else:
        return n + sum_num(n-1)  # recursive case


def main():
    n = 5
    print(sum_num(n))


main()
