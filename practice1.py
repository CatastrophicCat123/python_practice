'''
Your Task:
Write a Python program that calculates the final price of an item after applying a discount. Modify the code below by replacing the comments that say # YOUR CODE HERE with your code.

The original price of the item is $75.

The discount is 15%.

Your program should:

Store the original price and discount in variables.

Calculate the discount by dividing discount_rate by  100 and then multiplying by the original_price.

Calculate the final price by subtracting discount from the original_price.  

Print the final price with a clear message.
'''


original_price = 75
discount_rate = 15
discount = discount_rate / 100
final_price = original_price - original_price * discount
print(f"The final price after discount is: ${final_price}")