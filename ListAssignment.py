# 1- write a program which takes single input from user containing first name,
# last name and age as comma separated value and
# display then in 3 lines in given format below.
# example user input : Ankit,Bansal,35
# output:
# First name is Ankit
# last name is Bansal
# Ankit is 35 years old
user_input = input("enter first name,last name and age (separated by comma): ")
user_list = user_input.split(",")
print(f"First name is {user_list[0]}"+"\n"+f"Last name is {user_list[1]}"+"\n"+f"{user_list[0]} is {user_list[2]} years old")
# OR
user_input = input("enter first name,last name and age (separated by comma): ")
user_list = user_input.split(",")
first_name = user_list[0]
last_name = user_list[1]
age = user_list[2]
# Display the information
print("First name is", first_name)
print("Last name is", last_name)
print(first_name, "is", age, "years old.")
##############################
# 2- given 2 list as list1= [1,3,4] and list2 = [2,4,6]
# combined the 2 list and display the same without using extend method
list1 = [1, 3, 4]
list2 = [2, 4, 6]
list3 = list1 + list2
print("Result is : ", list3)

############
# 3- given a list list1=[1,2,3,4,5,6,7,8]
# display a new list which contains only odd position index values from above list.
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print("odd position index values are: ", list1[0::2])

#############
# 4- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a ipl team name as input from user and display a list of all elements from that name.
# example : input : KKR
# output : ['KKR','LSG','PBKS']
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
user_ipl = input("enter your team: ")
print(ipl["List of elements from the team name:", ipl.index(user_ipl):])

########
# 5- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a ipl team name as input from user and display a list of all elements except input one
# example : input : KKR
# output : ['CSK','MI','LSG','PBKS']
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
new_team = ipl.remove(input("enter the team you want to remove"))
print("List of elements except the input team:", ipl)
# OR
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
team_name = input("Enter the IPL team name: ")
team_elements = ipl.copy()
team_elements.pop(ipl.index(team_name))
print("List of elements except the input team:", team_elements)
#############

# 6- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma separated values index,new_team . replace the index element of list with new value and display the same
#
# example : input : 2,SRH
# output : ['CSK','MI','SRH','LSG','PBKS']
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
user_input1 = input("Enter index,new_team(comma separated): ")
index, newteam = user_input1.split(",")
index = int(index)
ipl[index] = newteam
print(ipl)
#################
# 7- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take ipl team name as user input. display True if the team exists else display False.
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
user = input("enter input")
if user in ipl:
    print("True")
else:
    print("False")
# or
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
team_name = input("Enter the IPL team name: ")
team_exists = team_name in ipl
print(team_exists)
#################
# 8-ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma separated values index,new_team . Add the new value at that index in the list.
# Display the old list , new list,length of original and new list
#
# example : input : 2,SRH
# output :
# old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
# new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
user_input1 = input("Enter index,new_team(comma separated): ")
index1, newteam1 = user_input1.split(",")
index1 = int(index1)
ipl2 = ipl.copy()
ipl2.insert(index1, newteam1)
print("old list : ", ipl, "and length: ", len(ipl))
print("new list : ", ipl2, "and length: ", len(ipl2))
