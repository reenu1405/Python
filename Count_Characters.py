# Count_Characters

# write a python function that accepts a string and prints the count of occurrence of each characters
# sample string: aabccda
# expected result:
# a -> 3
# b-> 1
# c-> 2
# d -> 1
def CountCharac(string):
    chardict = {}
    for char in string:
        if char in chardict:
            chardict[char] += 1
        else:
            chardict[char] = 1
    for char, count in chardict.items():
        print(char, "=", count)


char_input = input("Enter the string:")
char_res = CountCharac(char_input)
