#this is the start of the program
print("Hello, welcome")
first_name = input("Please enter your first name: ")
persons_age = int(input("Please enter your age: "))
meal_list = ["Standard","Vegetarian","Dairy-Free","No meal"]
activity_list = ["Music Jam Session","Science Experiments Lab","Sports Leadership Training"]
other_list = [2,3,4,"easy","moderate","challenging","$5 fee","$10 fee","$12 fee"]
#all variable initialised to 0
list_count = 0
list_cut = 0
list_cut0 = 0
list_cut1 = 0
fee = 5
meal_fee = 7
#print lines
print("Choose an activity: ")
print(f'1. {activity_list[0]} ({other_list[0]} hours, {other_list[3]}, {other_list[6]})')
print(f'2. {activity_list[1]} ({other_list[1]} hours, {other_list[4]}, {other_list[7]})')
print(f'3. {activity_list[2]} ({other_list[2]} hours, {other_list[5]}, {other_list[8]})')
#The user enters the chosen activity
ask1 = input("Enter the number of your chosen activity: ")
print("Choose a meal option")
print(f'1. {meal_list[0]} .')
print(f'2. {meal_list[1]} .')
print(f'3. {meal_list[2]} .')
print(f'4. {meal_list[3]} .')
#the user eneter the chosen meal choice
ask2 = int(input("Enter the number of your meal choice: "))
#calculating the results
if ask1 == '1':
    list_count = 0
    list_cut = list_count
    list_cut0 = list_count + 3
    list_cut1 = list_cut0 + 3
elif ask1 == '2':
    list_count = 1
    list_cut = list_count
    list_cut0 = list_count + 3
    list_cut1 = list_cut0 + 3
    fee = fee + 7
if ask2 == '4' :
    meal_fee = 0

overall_fee = fee + meal_fee
#printing the results
print(f'{first_name}, age {persons_age}, has chosen {activity_list[list_count]}, with {meal_list[ask2]}')
print("The following activity will include:")
print(f'{other_list[list_count]} hours of practice, Its {other_list[list_cut0]} and a {other_list[list_cut1]}')
print(f"overall, the cost comes to ${overall_fee}")
#asking for attendence
attend = input ("Are you going to be attending (yes or no): ")
if attend == "yes":
    print(f"{first_name} has comfrimed for {activity_list[list_count]}, see you there!")
elif attend == "no":
    print(f"{first_name} has not comfrimed for {activity_list[list_count]}.")