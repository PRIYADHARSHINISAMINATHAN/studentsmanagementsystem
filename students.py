students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent List:")
        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        search = input("Enter student name to search: ")

        if search in students:
            print("Student Found!")
        else:
            print("Student Not Found!")

    elif choice == "4":
        delete = input("Enter student name to delete: ")

        if delete in students:
            students.remove(delete)
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")