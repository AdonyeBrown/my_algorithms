def is_prime(number: int) -> bool:
    # this function checks if a number is prime or not.
    if number < 2:
        return False

    high = int(number**(1/2))
    for i in range(2, high):
        if number % i == 0:
            return False

    return True


number = 47
print(is_prime(number))
