'''Q2. You are analyzing purchase patterns in a retail store. each purchase record 
includes a customer ID and the amount spent. Write a program to find the 
customer who has made the highest number of purchases. Input: 4 
C005 120 
C006 80 
C005 200 
C007 150 
Output: C005 
2'''

n = 4
purchases = [ ["C005", "120"],["C006", "80"],["C005", "200"],["C007", "150"]]

# Dictionary to store both the count of purchases for each customer
purchase_data = {}

for record in purchases:
    customer_id = record[0]

    if customer_id in purchase_data:
        purchase_data[customer_id]['count'] += 1
    else:
        purchase_data[customer_id] = {'count': 1}

top_customer_by_count = None
max_purchases = 0

for customer_id, data in purchase_data.items():
    # Check for the most purchases
    if data['count'] > max_purchases:
        max_purchases = data['count']
        top_customer_by_count = customer_id

if top_customer_by_count:
    print(top_customer_by_count)
    print(max_purchases)


