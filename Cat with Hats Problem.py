## Cat with Hats Problem ##


# Question: Let say You have one 100 cats.
# One day, you decide to arrange all your cats in a giant circle.
# Initially,none of your cats has a hat on.
# You walk around the circle a 100 times, always starting with the first cat (cat #1).
# Each time you stop at a cat, you check if it has a hat on.
# If it does not, then you put a hat on it. If it does, then you take the hat off.
#
# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you stop only at every second cat (#2, #4, #6,
# #8, and so on).
# 3. The third round, you stop only at every third cat (#3, #6, #9, #12,
# and so on).
# 4. You continue this process until you’ve made one hundred rounds
# around the cats. On the last round, you stop only at cat #100.
#
#
# Write a program that simply outputs which cats have hats at the end.

# by default all are set to false since none have been visited
def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    # We want to walk around the circle 100 times
    for num in range(1, 100 + 1):
        # Each time we walk around, we visit 100 cats
        for cat in range(1, 100 + 1):
            # Determine whether to visit the cat
            # Use modulo operator to visit every 2nd, 3rd, 4th,... etc.
            if cat % num == 0:
                # Remove or add hat depending on
                # whether the cat already has one
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True
        # Add all number of each cat with a hat to list
    for cat in range(1, 100 + 1):
        if array_of_cats[cat] is True:
            cats_with_hats_on.append(cat)
    return cats_with_hats_on
cats = [False] * (100 + 1)
print(get_cats_with_hats(cats))

# solution : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
