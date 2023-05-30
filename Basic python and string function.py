
# que 1 #1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.
#BMI = weight / (square of height)
weight = float(input("Enter Weight in kgs"))
height = float(input("Enter height in mtrs"))
BMI = weight/(height)**2
print("Your BMI is ="+str(BMI))

print(f"Your BMI is = {BMI}")

# que 2:  write a program which takes the name of the user as input and replace all the occurence of character 'a' in the name to 'b' and print it.
name = input("Enter your name")
name2 = name.replace("a", "b")
print(f"your updated name is {name2}")

#que 3: write a program which takes 2 inputs from user as principle amount (int) and rate of annual interest (float) and print the expected total amount  after  2 years.
principle_amount = (int(input("enter the principle amount")))
rate = (float(input("enter the rate of annual interest in %")))
years = int(input("enter years"))
total_amount = (principle_amount * (1 + rate/100) ** years) 
print(f"your total amount is {total_amount}")

# que4 write a program which takes city name from user input. irrespective of in which case user enters the city name, print the city name in camel case meaning first letter should be capital and rest in small.
city_name = input("enter your city name")
city_case = city_name.capitalize()
city_Case = city_name.title()
print(f"your city is {city_case}")
print(f"your city is {city_Case}")


#ques 5 write a program which takes the name of the user as input and print the index of character 'a' in the string. if 'a' is not there then return -1.
name = input("enter your name")
index_name = name.find(input())
print(index_name)

#ques 6 Display the number of letters in the below string
my_word = "antidisestablishmentarianism"
my_word = "antidisestablishmentarianism"
len_1 = len(my_word)
print(len_1)



#ques 7take 3 inputs from user : first name , last name and age . Display the information in below format
# Display : my name is Mohit Sharma and I am 32 years old.
first_name = input("enter first name")
last_name = input("enter last name")
age = int(input("enter age"))
print(f"""first name : {first_name.capitalize()} 
last name : {last_name.capitalize()}  
age {age} """)
print(f"my name is {first_name.capitalize()} {last_name.capitalize()} and I am {age} years  old.")

first_name = input("enter first name")
last_name = input("enter last name")
age = int(input("enter age"))
print("first name :"+first_name.capitalize()+"\n"+"last name :"+last_name.capitalize()+'\n'+"age :" + str(age))


#ques 8take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.  Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
#Display : morma@infosys.com 

first_name = input("enter first name").lower()
last_name = input("enter last name").lower()
company = input("enter company name").lower()
print(first_name[0:2] + last_name[-3:] + "@" + company + ".com")

first_name = input("enter first name")
last_name = input("enter last name")
company = input("enter company name")
print((first_name[0:2] + last_name[-3:] + "@" + company + ".com").lower())







