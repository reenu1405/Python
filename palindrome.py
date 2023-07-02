# palindrome

# Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam.
#
def palindrome(pal):
    pal = pal.lower() # Convert the string to lowercase for case insensitivity
    rev_pal = pal[::-1]  # Reverse the string
    print("reverse: ",rev_pal)
    if pal == rev_pal:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
ent = input("passed a string and check its palindrome or not: ")
result = palindrome(ent)
