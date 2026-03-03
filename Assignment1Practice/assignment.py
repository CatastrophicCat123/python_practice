import pandas as pd
import os

file_name = 'grocery_list.csv'

if os.path.exists(file_name):
    grocery_list_df = pd.read_csv(file_name)
    grocery_list = grocery_list_df["item"].tolist()
    user_input = None
    while user_input != 'Quit':
        user_input = input("Add grocery item: ")
        if user_input != 'Quit':
            grocery_list.append(user_input)
    print("New Grocery List: ", grocery_list)
    grocery_list_df = pd.DataFrame(grocery_list, columns=grocery_list_df.columns)
    grocery_list_df.to_csv(file_name, index=False)
else:
    print(f"Error: The file '{file_name}' was not found in the current directory.")