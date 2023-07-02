# Count_Uppercase_lowercase_letters
Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
#
# using empty lists
ss = []
ll = []
def counts(strs):
    # print(len(strs))
    for i in strs:
        if i.isupper():
            ss.append(i)

        elif i.islower():
            ll.append(i)
    print("Lowercase letters are: ", len(ll))
    print("Uppercase letters are: ", len(ss))
s1 = input("Enter the String: ")
count_str = counts(s1)

# print(count_str) : using strings
# or
def counts(strs):
    # print(len(strs))
    ss = 0
    ll = 0
    for i in strs:
        if i.isupper():
            ss += 1

        elif i.islower():
            ll += 1
    print("Lowercase letters are: ", ll)
    print("Uppercase letters are: ", ss)
s1 = input("Enter the String: ")
count_str = counts(s1)
