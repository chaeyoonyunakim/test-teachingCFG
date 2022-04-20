
trees = [
    {'leaf_colour': 'green', 'height': 2120},
    {'leaf_colour': 'green', 'height': 2300}]
new_tree = {
    'leaf_colour': 'green',
    'height': 1020
}
trees.append(new_tree)
print(trees)




# import random
# first_names = ['A', 'B', 'C']
# last_names = ['Kim', 'Smith', 'Bath']
# first = random.choice(first_names)
# last = random.choice(last_names)
# print(first, last)
#
# verbs = ['go', 'eat', 'drink', 'sleep']
# nouns = ['I', 'Chaeyoon', 'you']
# sentences = nouns + verbs + nouns


#
# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]





#
# place = {
#     'name': 'The Anchor',
#     'post_code': 'E14 6HY',
#     'street_number': '54',
#     'location': {
#         'longitude': 127},
#         'latitude': 63,
#     }
# }
# print(place['name'], '\n',
#       place['post_code'], '\n',
#       place['street_number'])
# #the values of name,
# #post_code
# #street_number from the dictionary
# print('longitude: ', place['location']['longitude'])
# print('latitude: ', place['location']['latitude'])





#
# student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
# count = 0
#
# for student_name in student_names:
#     count = count + 1
#
# print(count)









#
# #Create a list
# shopping_list = ['banana', 'apple']
# #if 'bread' is in the list,
# if 'bread' in shopping_list:
#       #add 'butter' to the shopping list.
#       shopping_list.append('butter')
#       print("reminder: add butter")
# else:
#       print("let's go")





#
# # Make a list of game scores
# scores = [10, 20, 30, 40, 50, 60, 3, 200, 70, 100]
# # Using list functions
# len(scores)
# max(scores)
# min(scores)
# # Outputs
# print("Number of scores: ", len(scores), "\n"
#       "Highest score:", max(scores), "\n"
#       "Lowest score:", min(scores)
# )
# Number of scores: 10
# Highest score: 200
# Lowest score: 3






# # Lists
# ("Chaeyoon", 20, "Python", 3.5) #tuple
# ["Chaeyoon", 20, "Python", 3.5] #list
#
# list[0]
#
# # Dictionaries
# {"Name": "Chaeyoon", "age": 20, "skill": "Python", "budget": 3.5}
#
# dic[0]




# carrots = int(input('How many carrots do you have? '))
# rabbits = 6
#
# if rabbits > carrots:
#     print('There are not enough carrots')
# elif rabbits < carrots:
#     print('There are too many carrots')
# else:
#     print('You have the right number of carrots')







# import random
# money = float(input('the amount you want to bet: '))
# number = int(input('pick your number: '))
# my_colour = int(input('pick your colour red 1/black 2 : '))
#
# def roulette_choice():
#     choice_number = random.randint(1, 1)
#     colour = random.randint(1, 1)
#     print ('choice_number: ', choice_number, 'colour :', colour)
#     if colour == my_colour & choice_number == number:
#         result = money * 100
#         print('case 3: ', result)
#     elif colour == my_colour | choice_number == number: #red or black
#         if colour == my_colour:
#             result = money
#             print('case 1: ', result)
#         elif choice_number == number:
#             result = money * 2
#             print('case 2: ', result)
#     else:
#         result = 0
#         print('case 4: ', result)
#     return result
#
# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]
#
# # for i in fruits:
# #     print(i['name'])
# #     print(i['colour'])
# #     print(i['price'])
#
# if fruits[0] == 'apple':
#     print (fruits[0])
#     print ('here apple')
# else:
#     print(fruits[0])
#     print ('no apple')
#
#
# import random
#
# first_name = ['red', 'green', 'blue']
# last_name = ['', '', '']
#
#
#
# chosen_colour = random.choice(colours)
#
# print(chosen_colour)
#
#
# apples = 100
# if apples > 90:
#     print('That is a sensible number of apples')
# elif apples > 50:
#     print('This is too many apples')
# elif apples > 30:
#     print('That is not enough apples')
# else:
#     print('rest of apples')
#
# pokemon[] = {name: ['Chaeyoon', 'Lu', 'CJ'],
#          age: [35, 30, 30]}
#
# access = API
#
# for n in input:
#     if n['name'] < 3:
#         print(n)
#     else:
#         print('skip')