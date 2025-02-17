# Rabbit is very particular about his belongings and wants to own an even
# number of each thing he owns. Write a function can_pair() that accepts a
# list of integers item_quantities. Return True if each number in
# item_quantities is even.
#  Return False otherwise.


def can_pair(item_quantities):
    for item in item_quantities:
        if item % 2 != 0:
            return False

    return True


print(can_pair([2, 4]))

# you can also do a one-liner by doing
# def can_pair(item_quantities):
#   return all(item % 2 == 0 for item in item_quantities)
