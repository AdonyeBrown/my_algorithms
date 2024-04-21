def num(n):
    # base case
    if n == 0:
        return
    else:
        print(n)
        num(n-1)  # recursive case

# recursive calls are stored in stacks in the memory so it can be access after code
# termimates


def main():
    n = 5
    num(n)


main()
