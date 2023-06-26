 Perform list operations in Python, including indexing, list manipulation, and copy/clone list.
 # Lists : Indexing ,List Content ,List Operations, Copy and Clone List
 # About the Dataset :
Imagine you received album recommendations from your friends and compiled all of the recommandations into a table, with specific information about each album.

The table has one row for each movie and several columns:
artist - Name of the artist
album - Name of the album
released_year - Year the album was released
length_min_sec - Length of the album (hours,minutes,seconds)
genre - Genre of the album
music_recording_sales_millions - Music recording sales (millions in USD) on SONG://DATABASE
claimed_sales_millions - Album's claimed sales (millions in USD) on SONG://DATABASE
date_released - Date on which the album was released
soundtrack - Indicates if the album is the movie soundtrack (Y) or (N)
rating_of_friends - Indicates the rating from your friends from 1 to 10 */

# Create a list

L = ["Michael Jackson", 10.1, 1982]

# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )


# List Content
 Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples and other data structures. 
The same indexing conventions apply for nesting:
# Sample List
["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]

# List slicing
# Sample List
L = ["Michael Jackson", 10.1,1982,"MJ",1]
print(L[3:5])
result = ['MJ', 1]

# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)
['Michael Jackson', 10.2, 'pop', 10]

# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L
['Michael Jackson', 10.2, ['pop', 10]]

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

Before change: ['disco', 10, 1.2]
After change: ['hard rock', 10, 1.2]
  
  
# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)

Before change: ['hard rock', 10, 1.2]
After change: [10, 1.2]

# Split the string by comma

'A,B,C,D'.split(',')
['A', 'B', 'C', 'D']

# Split the string, default is by space

'hard rock'.split()
['hard', 'rock']

# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

A: ['hard rock', 10, 1.2]
B: ['hard rock', 10, 1.2]

# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

B[0]: hard rock
B[0]: banana

  # Clone (clone by value) the list A

B = A[:]
['banana', 10, 1.2]
# after cloning if we change any element in A it will not impact list B
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])
B[0]: banana
B[0]: banana

