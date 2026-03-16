#This is our validation variable, which will help us to break the loop while once the user has entered the expected value
validation = False

print("Welcome to your inventory management app!")
print(f"-" * 42)

#Here we will ask for the price and quantity of the product, but since we need to check if the value entered is valid, we will use the lop while combined with a try/except
while validation == False:
    productName = input("Please enter the name of the product: ")
    try:
        price = float(input("Please enter the price of your product: "))
        quantity = int(input("Please enter the quantity of products you want: "))
        validation = True 
    except:
        print("Please enter a valid parameter for each input.")

#Here we calculate the total cost of the sell 
totalCost = price * quantity

#Print the final result to the user 
print(f"-" * 73)
print(f"Name of the product: {productName} | Price: {price} | Quantity: {quantity} | Total Cost: {totalCost}")
print(f"-" * 73)
