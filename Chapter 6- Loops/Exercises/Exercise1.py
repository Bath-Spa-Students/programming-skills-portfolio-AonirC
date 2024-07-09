#loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value
prompt = "\nWelcome to Pizzaria! What topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        #print a message saying you'll add that topping to their pizza
        print("  I'll add " + topping + " to your pizza.")
    else:
        break
