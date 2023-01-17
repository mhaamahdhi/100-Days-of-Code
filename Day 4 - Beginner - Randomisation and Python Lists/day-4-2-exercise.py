import random

names_string = input("Give me everybody's names,seperated by a comma. :")
names = names_string.split(", ")

length_of_names = len(names)
random_pick_names =random.randint(0,length_of_names-1)
pick_name_from_list = names[random_pick_names]

print(f"{pick_name_from_list} is going to buy the meal today!")