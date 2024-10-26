#Declaring a variable


temperature = 22.0

name = "Liza"
print(type(temperature))
print(type(name))

age = 24

x=5
y=8

result = x+y

print(result)

#update value
age = age + 1
print(age)

#combine values

first_name = "Blerta"
last_name = "Hajdini"

full_name = first_name + " " + last_name
print(full_name)

#Lists

name_of_the_list = ["item 1" , "item2", "item 3"]

#example of a list

shopping_list = ["apples", "bananas", "milk", 3,4.5]
print(shopping_list)

#indeksimi

homework = ["math", "psikologji", "biologji", "anglisht"]
print(homework[0])
print(homework[3])
print(homework[1])

to_do_list = ["teach 11D", "Go shopping", "Create the app", "Check devops"]
first_item = to_do_list[0] #this is accessing the first item at index 0, which is "teach 11D"
second_item = to_do_list[1]
third_item = to_do_list[2]

favorite_subject = ["psikologji", "sociologji", "ed.fizike", "frengjisht",]
forth_subject = favorite_subject[3]
print(forth_subject)

#Adding Data to a list we do so by using the append() method
#I want to add strawberries to the shopping list

shopping_list.append("strawberries")
print(shopping_list)

#Insert method lets us specify where we want to add or element
shopping_list.insert(2, "lemons")
print(shopping_list)

#remove() methods help us remove items from the list

to_do_list.remove("check devops")
print(to_do_list)

del to_do_list [2]
print(to_do_list)

#updating data, you can change the value of an item by assigning a new value to an index
to_do_list[0] = "teach 1D"

print(to_do_list)