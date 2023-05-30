"""
# que 1
weight = float(input("Enter Weight in kgs"))
height = float(input("Enter height in mtrs"))
BMI = weight/(height)**2
print("Your BMI is ="+str(BMI))

print(f"Your BMI is = {BMI}")
"""
"""
# que 2
name = input("Enter your name")
name2 = name.replace("a", "b")
print(f"your updated name is {name2}")
"""
"""
#que 3
principle_amount = (int(input("enter the principle amount")))
rate = (float(input("enter the rate of annual interest in %")))
years = int(input("enter years"))
total_amount = (principle_amount * (1 + rate/100) ** years) 
print(f"your total amount is {total_amount}")
"""
"""
# que 4
city_name = input("enter your city name")
city_case = city_name.capitalize()
city_Case = city_name.title()
print(f"your city is {city_case}")
print(f"your city is {city_Case}")
"""
"""
#ques 5
name = input("enter your name")
index_name = name.find(input())
print(index_name)
"""
"""
#ques 6
my_word = "antidisestablishmentarianism"
len_1 = len(my_word)
print(len_1)
"""


#ques 7
first_name = input("enter first name")
last_name = input("enter last name")
age = int(input("enter age"))
print(f"""first name : {first_name.capitalize()} 
last name : {last_name.capitalize()}  
age {age} """)
print(f"my name is {first_name.capitalize()} {last_name.capitalize()} and I am {age} years  old.")
"""
first_name = input("enter first name")
last_name = input("enter last name")
age = int(input("enter age"))
print("first name :"+first_name.capitalize()+"\n"+"last name :"+last_name.capitalize()+'\n'+"age :" + str(age))

"""
#ques 8
"""
first_name = input("enter first name").lower()
last_name = input("enter last name").lower()
company = input("enter company name").lower()
print(first_name[0:2] + last_name[-3:] + "@" + company + ".com")
"""
first_name = input("enter first name")
last_name = input("enter last name")
company = input("enter company name")
print((first_name[0:2] + last_name[-3:] + "@" + company + ".com").lower())







