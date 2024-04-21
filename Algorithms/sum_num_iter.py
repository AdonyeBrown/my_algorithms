def sum_num_iter(n):
    for i in range(n+1):
        i += i
    return i + n


def main():
    n = 5
    print(sum_num_iter(n))


main()
