# List to store all student records 

students = [] 

 

# Function to calculate average 

def calculate_average(marks): 

    return sum(marks) / len(marks) 

 

# Function to calculate grade 

def calculate_grade(average): 

    if average >= 90: 

        return "A" 

    elif average >= 75: 

        return "B" 

    elif average >= 60: 

        return "C" 

    elif average >= 40: 

        return "D" 

    else: 

        return "Fail" 

 

# Function to add student 

def add_student(): 

    name = input("Enter student name: ") 

    marks = [] 

 

    n = int(input("How many subjects? ")) 

    for i in range(n): 

        mark = float(input(f"Enter marks for subject {i+1}: ")) 

        marks.append(mark) 

 

    student = { 

        "name": name, 

        "marks": marks 

    } 

    students.append(student) 

    print("Student added successfully!\n") 

 

# Function to display all students 

def display_students(): 

    if not students: 

        print("No student records found.\n") 

        return 

 

    for student in students: 

        name = student["name"] 

        marks = student["marks"] 

        average = calculate_average(marks) 

        grade = calculate_grade(average) 

 

        print(f"Name: {name}") 

        print(f"Marks: {marks}") 

        print(f"Average: {average:.2f}") 

        print(f"Grade: {grade}") 

        print("-" * 30) 
 
# Function to search a student 

def find_student(): 

    search_name = input("Enter student name to search: ") 

    for student in students: 

        if student["name"].lower() == search_name.lower(): 

            marks = student["marks"] 

            average = calculate_average(marks) 

            grade = calculate_grade(average) 

            print(f"\nName: {student['name']}") 

            print(f"Marks: {marks}") 

            print(f"Average: {average:.2f}") 

            print(f"Grade: {grade}\n") 

            return 
        
    print("Student not found.\n") 
# Menu-driven program 

while True: 

    print("1. Add Student") 

    print("2. Display All Students") 

    print("3. Search Student") 

    print("4. Exit") 

    choice = input("Enter your choice: ") 

    if choice == "1": 

        add_student() 
    elif choice == "2": 

        display_students() 
    elif choice == "3": 

        find_student() 
    elif choice == "4": 

        print("Exiting program...") 

        break 

    else:
        print("Invalid choice. Try again.\n") 