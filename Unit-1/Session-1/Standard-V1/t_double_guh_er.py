# Signs in the Hundred Acre Wood have been losing letters as Tigger
# bounces around stealing any letters he needs to spell out his name.
# Write a function tiggerfy() that accepts a string s, and returns a new
# string with the letters t, i, g, e, and r removed from it


def tigerfy(s):
    action = "tiger"
    action = list(action)
    s = s.lower()
    s = list(s)

    for item in action:
        while item in s:
            s.remove(item)

    s = "".join(s)

    return s


print(tigerfy("suspicerous"))
