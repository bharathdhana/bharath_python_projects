#From the List of Strings to perform iterations:
list_str =  ["apple", "banana", "cherry", "date", "fig"]

print("Original List:",list_str)
for item in list_str:
    if item == "cherry":
        continue
    print("Elements of the list:",item)
