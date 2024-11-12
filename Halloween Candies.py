'''Halloween Candies

Bob goes to super market to shop candies represented by an array A for halloween party, his mother gave him some money M. due to the festive season, there are several offers inthe supermarket. One such offer useful for Bob is, if the price of the candy is a multiple of 5, he can buy it without spending any money otherwise he will spend money equal to A which is the price of a particular candy. bob can shop as long he has money. Your task is to find and return the maximum number of candies Bob can buy

Input Specification:
input1:An integer value, representing number of candies
input2:An integer array A, representing presenting price of each candy.
input3:An integer value M, representing the amount of money

Output Specification:Return the number of candies Bob can buy
'''

def max_candies(num_candies, prices, money):
    free_candies = 0
    paid_candies = []

    # Separate free and paid candies
    for price in prices:
        if price % 5 == 0:
            free_candies += 1  # Candy is free
        else:
            paid_candies.append(price)  # Candy costs money

    # Sort the paid candies by price (cheapest first)
    paid_candies.sort()

    # Count the total number of candies Bob can buy
    total_candies = free_candies

    # Buy as many paid candies as possible with the money he has
    for price in paid_candies:
        if money >= price:
            money -= price
            total_candies += 1
        else:
            break  # Stop if not enough money for the next candy

    return total_candies

num_candies = 6
prices = [4, 7, 5, 2, 15, 20]
money = 7
print(max_candies(num_candies, prices, money))  
