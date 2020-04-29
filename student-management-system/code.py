# --------------
# Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua','Bengio']
class_2 = ['Hilary','Mason','Carla Gentry','Corinna cortes']

# Create the lists 

# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)



# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)


# Remove the element from the list
new_class.remove('Carla Gentry')


# Print the list
print(new_class)



# Create the Dictionary
courses = {'Math':65,'English':70,'Histroy':80,'French':70,'Science':60} 




# Slice the dict and stores  the all subjects marks in variable
Total = 65+70+80+70+60


# Store the all the subject in one variable `Total`

# Print the total
print(Total)

# Insert percentage formula
percentage = Total/500*100

# Print the percentage
print(percentage)




# Create the Dictionary
mathematics = {'Geoffrey Hinton':78,'Andrew Ng': 95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes': 66,'Peter Warden': 75}
max_marks_scored = max(courses,key = courses.get)
print(max_marks_scored)
highest_in_mathematics = max(mathematics,key = mathematics.get)
print(highest_in_mathematics)

 



# Given string
topper = 'Andrew Ng'




# Create variable first_name 
first_name = 'Andrew'



# Create variable Last_name and store last two element in the list
last_name = 'Ng'


# Concatenate the string
Name = last_name +' '+ first_name

# print the full_name
print(Name)
certificate_name= Name.upper()

# print the name in upper case
print(certificate_name)


# Code ends here


