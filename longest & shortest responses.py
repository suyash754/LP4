'''You conducted a survey and collected responses in the form of strings. each 
response is a sentence. Write a program that finds the longest and 
shortest responses. '''
def main():
    responses = ["Yes","No","Absolutely","Maybe","I'm not sure about that","Okay"]
    
    # Initialize both variables with the first response in the list
    largest_response = shortest_response = responses[0]
    
    # Loop through the list starting from the second element
    for response in responses[1:]:
        if len(response) > len(largest_response):
            largest_response = response
        elif len(response) < len(shortest_response):
            shortest_response = response
    
    print(f"Largest Response: {largest_response}")
    print(f"Shortest Response: {shortest_response}")

main()
