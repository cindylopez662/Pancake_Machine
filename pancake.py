import sys, math


if __name__ == "__main__":
#Pancake Time
   
    #This is the minimum and it will equal 6 pancakes in a small pan
    #Everything will be in cups excluding the oil - it will be in tablespoons
    
    pancake_recipe = {
    'pancake_mix': 1.0,
    'milk' : 0.75,
    'eggs' : 1 
    } 

    greeting = 'Hello, user! You want to make pancakes? Perfect! I am here to help.'
    print(greeting)
    print("You will need:\n{} cup of pancake mix\n{} cups of milk and \n{} eggs".format(
        pancake_recipe['pancake_mix'], 
        pancake_recipe['milk'], 
        pancake_recipe['eggs']))

    mix_question = 'Tell me how many cups of pancake mix you have: '
    mix_amount = float(input(mix_question))

    print("You have {amount} cups of pancake mix".format(amount = mix_amount))

    milk_question = 'Tell me how many cups of milk you have: '
    milk_amount = float(input(milk_question))
    print("You have {amount_2} cups of milk".format(amount_2 = milk_amount))

    egg_question = 'Tell me how many eggs you have: '
    egg_amount = int(input(egg_question))
    print("You have {amount_3} eggs".format(amount_3 = egg_amount))

    calculating = 'One moment please!'
    print(calculating)

    #main code 

    if pancake_recipe["pancake_mix"] > mix_amount :
        print("You do not have enough pancake mix to make a batch of 6 pancakes")
        sys.exit(0)

    if pancake_recipe["milk"] > milk_amount :
        print(" You do not have enough milk to make a batch of 6 pancakes")
        sys.exit(0)

    if pancake_recipe["eggs"] >  egg_amount :
        print("You do not have enough eggs to make a batch of 6 pancakes")
        sys.exit(0)

    # maths
    mix_total_amount = math.floor(mix_amount / pancake_recipe["pancake_mix"])
    print("You have {total} usable cups of flour".format(total = mix_total_amount))

    milk_total_amount = math.floor(milk_amount / pancake_recipe["milk"])
    print("You have {total} usable 3/4 cups of milk".format(total = milk_total_amount))

    print("You have {amount_3} eggs".format(amount_3 = egg_amount))

    # calc how many pancakes you can make

    amount_ycm = "With these ingredients you can make {} pancakes"
    min_avail = min(mix_total_amount, milk_total_amount, egg_amount)
    print(amount_ycm.format(min_avail*6))
    print("You will need to use: ")
    print("{} cups of pancake mix".format(min_avail))
    print("{} - 3/4 cups of milk".format(min_avail))
    print("{} egg(s)".format(min_avail))

    reminder = 'Remember to use a dash of vegetable oil as well!'
    print(reminder)