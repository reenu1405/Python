

# 1- write a function called find_common_elements that takes two lists as input and
# returns a new list containing the common elements between the two lists.
def find_common_elements(L1,L2):
    L3 = []
    for i in L1:
        for j in L2:
            if i == j:
                L3.append(i)
    return L3
list11 = input("Enter the elements separated by comma")
list1 = list11.split(',')
list21 = input("Enter the elements separated by comma")
list2 = list21.split(',')
List_result = find_common_elements(list1,list2)
print(List_result)

# or
def find_elements(L1,L2):
     common_elements = []
     for i in L1:
         if i in L2:
             common_elements.append(i)
     return common_elements
inputL1 = [1,2,35,6,7,8,9]
inputL2 = [9,76,55,88,35,2,1,77]
common = find_elements(inputL1,inputL2)
print("Common elements are: ", common)
