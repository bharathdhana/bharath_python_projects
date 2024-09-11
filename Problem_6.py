#Get the inputs and print the sum and average:
def get_input():
    ele1 = int(input("Enter value a:"))
    ele2 = int(input("Enter value b:"))
    ele3 = int(input("Enter value c:"))

    total = sum([ele1,ele2,ele3])
    print("Total of inputs:",total)
    average = total / 3
    print("Average of inputs:",average)

get_input()
