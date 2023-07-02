# Distinct_Elements

Write a Python function that takes a list and returns a new list with
# distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
lst1 = [1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7]
result_lst = list(lst1)
