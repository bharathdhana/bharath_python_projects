#Random Numbers from 1 to 50
import random
def assign_values_to_name(name):
    random_value = random.randint(1,50)
    print(f"The value assigned to {name} is {random_value}")


user_name = input("Enter your name:")
assign_values_to_name(user_name)
