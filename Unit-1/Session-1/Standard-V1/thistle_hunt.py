# Pooh, Piglet, and Roo are looking for thistles to gift their friend
# Eeyore. Write a function locate_thistles() that takes in a list of strings
# items and returns a list of the indices of any elements with value "thistle".
# The indices in the resulting list should be ordered from
# least to greatest.


def locate_thistles(items):
    word = "thistle"
    indices = []
    for index, value in enumerate(items):
        if items[index] == word:
            indices.append(index)

    return indices


print(locate_thistles(["book", "bouncy ball", "leaf", "red balloon"]))
