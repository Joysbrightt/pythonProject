

twitter_users = [
    {"Username": "@Chidezo", "age": 30, "Tweet": ["Twitter is a good place to be for developers", "Python is most beautiful language to write"]},
    {"Username": "Jaleko", "Ifalere" "age": 25, "Tweet": "I am single and searching"},
    {"Username": "Jekoyemi" "johnson", "age": 20, "Tweet": []},
    {"Username": "Joseph" "John", "age": 28, "Tweet": ["Twitter is a good place to be for developers", "I am into python programming and Koktlin and like folllow"]},
    {"Username": "barney" ,"Doe": 30, "Tweet": "Twitter is a good place to be for developers"},
    {"Username": "Josley" "Ashley","age": 26, "Tweet": ["Marketing your skill is all about letting people know about what you do"]},
    {"Username": "Mount" "Mason","age": 19, "Tweet": ["Twitter is a good place to be for developers", "Python is most beautiful language to write"]},
    {"Username": "Anthonio" "Thorgan","age": 29, "Tweet": ["Twitter is a good place to be for developers", "Python is most beautiful language to write"]},
    {"Username": "Joysbright" "Kingsley","age": 24, "Tweet": ["Twitter is a good place to be for developers", "Python is most beautiful language to write"]},
    {"Username": "Fred" "Angy","age": 20, "Tweet": ["Twitter is a good place to be for developers", "Python is most beautiful language to write"]},
    {"Username": "Chideko" "Chichi","age": 22, "Tweet": ["Motivation is the for the weak, and people who don't what their journey in life", "Python is most beautiful language to write"]},

]
# using list comprehension
getting =[user["username"] for user in twitter_users if user[verified] = is True]
print()

# mapping
getting2 =filter(lambda x: x['username'], if x['verified'] else False, twitter_users )
# using map
getting2 = map(lambda y: y['username'],filter(lambda x: x['verified'] ,twitter_users)

# doing map in reverse
getting3 = map(lambda x:x['username'] if x('verified') else False, twitter_users)
getting3 = filter(lambda x: x, map(lambda x:x['username'] if x('verified') else False, twitter_users))
# another way including the filter and map

print(list(getting3))

# worked but not accepted
getting2 = map(lambda x: x, [user["username"] for user in twitter_users if user[verified] = is True])



# getting list of active users
getting =[user["username"] for user in twitter_users if len(user['tweets']) = > 0]


# get the list of user that are below 25 and are verified
getting =[user["username"] for user in twitter_users if user['age'])  < 25 and user['verified']


# get the max, min, and average
getting_age =max([user["age"] for user in twitter_users ])
# getting minimum age in the list
getting_age =min([user["age"] for user in twitter_users ])

#getting the average
getting_age =average([user["age"] for user in twitter_users / len(twitter_users) ])
print(getting_age)

# using reduce to find average age in the list
from functools import reduce

avg2 = reduce(lambda x, y: x + y, (user('age') for user in twitter_users) / len(twitter_users))
print(avg2)

# using statistics to sovle find average in a list
from statistics import mean
print(mean(user['age'] for user in twitter_users))


# finding the the user with the most tweet in a list
most_tweets = max(twitter_users, key=lambda user: len(user['tweets']))

# finding the user with the most tweet in a list and return only the tweet

most_tweets = max(twitter_users, key=lambda user: len(user['tweets']))['tweets']
print(most_tweets)

# sorting in an ascending order
ascend = sorted(twitter_users, key=lambda user: user['age'], reverse=True)

