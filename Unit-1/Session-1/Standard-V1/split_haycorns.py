# Piglet's has collected a big pile of his favorite food, haycorns,
# and wants to split them evenly amongst his friends. Write a function
# split_haycorns() to help Piglet determine the number of ways he can
# split his haycorns into even groups. split_haycorns() accepts a
# positive integer quantity as a parameter and returns a list of all divisors
# of quantity.


def split_haycorns(quantity):
    divisors = []
    mid = quantity // 2

    for i in range(1, mid + 1):
        if quantity % (i) == 0:
            divisors.append(i)

    divisors.append(quantity)

    return divisors


print(split_haycorns(78))
