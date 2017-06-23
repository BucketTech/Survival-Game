import random
global food
global water
global alive
food = 50
water = 50
alive = 1


def day():
    activity = imput('what would you like to do')
    if activity=('find food'):
        print('you search for food')
        foodFound = random.randint(1,10)
        food+= food
        print('you found ',foodFound,' food')
    elif activity=('find water'):
        print('you search for water')
        waterFound = random.randint(1,10)
        water += waterFound
        print('you found ',waterFound,' water')
        print('you have ', food, ' food and ', water, ' water')

    food -= random.randint(1, 3)
    water -= random.randint(1, 3)
    days_survived = days_survived + 1
    print('you have survived ', days_survived, 'days')


day()
# its very basic i will make a better version asap this is for idea purposes only
