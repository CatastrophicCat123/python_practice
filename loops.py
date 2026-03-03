''' Simple For Loop '''
for i in range(1, 11):
    print(i)

celsius_temperatures = [0, 10, 25, 32, 100]
for celsius in celsius_temperatures:
    print(celsius)



''' While Loop: Executing based on conditions '''
valid_input = False
while not valid_input:
    user_input = int(input("Please enter a number greater than 0: "))
    if user_input > 0:
        valid_input = True
    else:
        print("Invalid input. Please try again.")

