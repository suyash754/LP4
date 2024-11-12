''' You are keeping track of sales in a bakery. Each sale amount is represented by 
an integer. Write a program that calculates the total sales and the average sale 
amount. '''

n = 4
sales = [10.5, 20.75, 30.2, 40.1]

total_sales = sum(sales)

average_sales = total_sales / n

# Print the results with 2 decimal places
print(f"Total Sales: {total_sales:.0f}")
print(f"Average Sale Amount: {average_sales:.2f}")
