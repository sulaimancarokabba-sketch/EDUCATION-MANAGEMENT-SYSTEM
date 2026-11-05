
# =====================================================
# EDUCATION MANAGEMENT SYSTEM
# PROG211 - OBJECT-ORIENTED PROGRAMMING 1
# Topic: Student Learning Portal
# =====================================================


# CLASS 1: STUDENT
class Student:

    # Class attribute
    total_students = 0

    def __init__(self, student_id, name, course, mark):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.mark = mark

        Student.total_students += 1

    # Instance method: Update student record
    def update_record(self, course, mark):
        self.course = course
        self.mark = mark
        print("\nStudent record updated successfully!")

    # Instance method: Display student information
    def display_info(self):
        print("--------------------------------")
        print("STUDENT INFORMATION")
        print("--------------------------------")
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("Course:", self.course)
        print("Examination Mark:", self.mark)

        if self.mark >= 50:
            print("Result: PASS")
        else:
            print("Result: FAIL")

    # Class method: Count registered students
    @classmethod
    def get_total_students(cls):
        return cls.total_students


# CLASS 2: EDUCATION PORTAL
class EducationPortal:

    def __init__(self):
        # Python list stores multiple student objects
        self.students = []

    # Add a new student
    def add_student(self):

        print("\n===== REGISTER NEW STUDENT =====")

        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        # Check for duplicate student ID
        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Student Name: ").strip()
        course = input("Enter Course Name: ").strip()

        if not name or not course:
            print("Name and course cannot be empty.")
            return

        try:
            mark = float(input("Enter Examination Mark (0-100): "))

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100.")
                return

        except ValueError:
            print("Invalid mark. Please enter a number.")
            return

        # Create a Student object
        new_student = Student(student_id, name, course, mark)

        # Store the object in the list
        self.students.append(new_student)

        print("\nStudent registered successfully!")

    # Display all student records
    def display_students(self):

        print("\n===== ALL REGISTERED STUDENTS =====")

        if not self.students:
            print("No student records available.")
            return

        for student in self.students:
            student.display_info()

        print("--------------------------------")
        print("Total Students:",
              Student.get_total_students())

    # Search for a student
    def search_student(self):

        print("\n===== SEARCH STUDENT =====")

        student_id = input("Enter Student ID: ").strip()

        for student in self.students:

            if student.student_id == student_id:
                student.display_info()
                return

        print("Student not found!")

    # Update student academic record
    def update_student(self):

        print("\n===== UPDATE STUDENT RECORD =====")

        student_id = input("Enter Student ID: ").strip()

        for student in self.students:

            if student.student_id == student_id:

                new_course = input("Enter New Course: ").strip()

                if not new_course:
                    print("Course cannot be empty.")
                    return

                try:
                    new_mark = float(
                        input("Enter New Examination Mark: ")
                    )

                    if new_mark < 0 or new_mark > 100:
                        print("Mark must be between 0 and 100.")
                        return

                except ValueError:
                    print("Invalid examination mark.")
                    return

                student.update_record(new_course, new_mark)
                return

        print("Student not found!")

    # Main application menu
    def run(self):

        while True:

            print("\n===================================")
            print("     EDUCATION MANAGEMENT SYSTEM")
            print("          STUDENT PORTAL")
            print("===================================")

            print("1. Register Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Update Student Record")
            print("5. Total Registered Students")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.display_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                print(
                    "\nTotal Registered Students:",
                    Student.get_total_students()
                )

            elif choice == "6":
                print("\nThank you for using the Education Management System!")
                break

            else:
                print("\nInvalid choice! Please try again.")


# MAIN PROGRAM
if __name__ == "__main__":

    # Create an EducationPortal object
    portal = EducationPortal()

    # Start the application
    portal.run()
