# Function to input student details and marks
def input_details_Student():
    name = input("Enter Student Name: ")
    std_class = input("Enter the Student's class: ")
    sec = input("Enter the Student's section: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter the mark for subject {i}: "))
        marks.append(mark)

    return name, std_class, sec, marks

# Function to calculate total marks and percentage
def calculate_total_and_percentage(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100  # Assuming each subject is out of 100
    return total_marks, percentage

# Function to display student result
def student_result(name, std_class, sec, total_marks, percentage):
    print("---Student Result---")
    print("--------------------")
    print(f"Name: {name}")
    print(f"Class: {std_class}")
    print(f"Section: {sec}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")

# Main function to run the program
def main():
    name, std_class, sec, marks = input_details_Student()
    total_marks, percentage = calculate_total_and_percentage(marks)
    student_result(name, std_class, sec, total_marks, percentage)

# Executing the main function
if __name__ == "__main__":
    main()
