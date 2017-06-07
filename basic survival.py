import random
global food
food=50
global water
water=50
global alive
alive=1

def day():
    days_survived=0
    while days_survived<100:
        global food
        global water
        if input('do you want to look for food(Y/N)')==('Y'):
            food_found=random.randint(3,10)
            food=food+food_found
            print('you found +',food_found,' food') 
            if random.randint(1,2)==2:
                print('an animal attacks (-5 food -2 water)')
                water=water-2
                food=food-5
            else:
                print('you made it home safe')
        elif input('do you want to look for water(Y/N)')==('Y'):
            water_found=random.randint(3,10)
            water=water+water_found
            print('you found +',water_found,' water')
            if random.randint(1,2)==2:
                print('an animal attacks (-5 water -2 food)')
                water=water-5
                food=food-2
            else:
                print('you made it home safe')
        food=food-random.randint(1,3)
        water=water-random.randint(1,3)
        print('you have ',food,' food and ',water,' water')
        days_survived=days_survived+1
        print('you have survived ',days_survived,'days')
        
    




day()
       #its very basic i will make a better version asap this is for idea purposes only 
    
