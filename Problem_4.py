#List of values from user:
def list_from_user(prompt):
    user_input = input(prompt)
    return user_input.split()

keys = list_from_user("Enter the keys:")
values = list_from_user("Enter the values:")

if len(keys) != len(values):
    print("The number of keys and values do not match.")
else:
    user_dict = dict(zip(keys,values))
    print("Resulting dictionary:",user_dict)
