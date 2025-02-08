# Help Winnie the Pooh double his honey! Write a function doubled() that accepts
# a list of integers hunny_jars as a parameter and multiplies each element
# in the list by two.
# Return the doubled list.


def doubled(hunny_jars):
    result = [(value * 2) for value in hunny_jars]

    return result


print(doubled([2, 4, 6]))
