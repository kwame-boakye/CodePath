# Write a function madlib() that accepts one parameter, a string verb.
# The function should print the sentence:
# "I have one power. I never <verb>. - Batman".


def madlib(verb):
    return f"I have one power. I never {verb}. - Batman"


print(madlib("nap"))
print(madlib("give up"))
