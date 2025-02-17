# Write a function print_todo_list() that accepts a list
# of strings named tasks. The function should then number and print each
# task on a new line using the format:

# Pooh's To Dos:
# 1. Task 1
# 2. Task 2


def print_to_do_list(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {tasks[i - 1]}\n")


# To do a 1-based indexing in numbering the items in the list,
# you can do:
# 1. for i in range(1, len(tasks) + 1) and access tasks[i - 1]
# 2. for i, task in enumerate(tasks, start=1) and also access tasks[i - 1]

print(
    print_to_do_list(
        [
            "Count all the bees in the hive",
            "Chase all the clouds from the sky",
            "Think",
            "Stoutness Exercises",
        ]
    )
)
