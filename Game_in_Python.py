def game():
    numbers_list = []
    door_choice = input("Select a door (red or yellow): ").lower()
    if door_choice == "red":
       number_choice = int(input("Select a number from 1 to 5: "))
       if number_choice in [1, 4]:
            for i in range(3):
                num = int(input(f"Enter number {i+1} from 1 to 100: "))
            while num < 1 or num > 100:
                print("Number out of range. Please enter a number between 1 and 100.")
                num = int(input(f"Enter number {i+1} from 1 to 100: "))
            numbers_list.append(num)
       elif number_choice in [2, 3, 5]:
            
            print("You lost.")
            return
       else:
            print("Invalid choice. Please select a number from 1 to 5.")
            return

    elif door_choice == "yellow":
        number_choice = int(input("Select a number from 6 to 10: "))
        if number_choice in range(6, 11):
            if number_choice % 2 == 0:
                for i in range(3):
                    num = int(input(f"Enter number {i+1} from 1 to 100: "))
                    while num < 1 or num > 100:
                        print("Number out of range. Please enter a number between 1 and 100.")
                        num = int(input(f"Enter number {i+1} from 1 to 100: "))
                    numbers_list.append(num)
            else:
                print("You lost.")
                return
        else:
            print("Invalid choice. Please select a number from 6 to 10.")
            return
    else:
        print("Invalid door choice. Please select either 'red' or 'yellow'.")
        return

    # Check if the sum of the list is greater than 130 and lesser than 1079
    total_sum = sum(numbers_list)
    if 130 < total_sum < 1079:
        print("You win.")
    else:
        print("You lost.")

# Start the game
game()



























