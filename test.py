print("Hello, welcome")
first_name = input("Please enter your first name: ")
persons_age = int(input("Please enter your age: "))
meal_list = ["Standard","Vegetarian","Dairy_Free","No meal"]
activity_list = ["Music Jam Session","Science Experiments Lab","Sports Leadership Training"]
other_list = [2,3,4,"easy","moderate","challenging","$5 fee","$10 fee","$12 fee"]
list_cut = 0
list_cut0 = 0
list_cut1 = 0
fee = 5
meal_fee = 7
print("Choose an activity: ")
print(f'1. {activity_list[0]} ({other_list[0]} hours, {other_list[3]}, {other_list[6]})')
print(f'2. {activity_list[1]} ({other_list[1]} hours, {other_list[4]}, {other_list[7]})')
print(f'3. {activity_list[2]} ({other_list[2]} hours, {other_list[5]}, {other_list[8]})')
ask1 = input("Enter the number of your chosen activity")
print("Choose a meal option")
print(f'1. {meal_list[0]} .')
print(f'2. {meal_list[1]} .')
print(f'3. {meal_list[2]} .')
print(f'4. {meal_list[3]} .')