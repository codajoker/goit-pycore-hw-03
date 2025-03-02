import random
def get_numbers_ticket(min, max, quantity) :
    # try :
        if(min <= 0) :
            print("min meed more than zero")
        elif (max > 1000) : 
            print("max meed less than 1000")
        elif (quantity > (max - min) ) :
            print (f"quantity meed less than {max - min}")
        array_random_number = []
        for i in range (quantity):
            random_number = random.randint(min, max)
            array_random_number.append(random_number)
        print(array_random_number)
            
    # except :
    #     print("Invalid  format")

get_numbers_ticket(1, 49, 6)
