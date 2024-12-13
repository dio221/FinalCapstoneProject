class Employee:
    def __init__(self, employee_id, name, organization):
        self.employee_id = employee_id
        self.name = name
        self.organization = organization
        self.attendance = []

    def mark_attendance(self, present):
        self.attendance.append(present)

    def calculate_attendance_percentage(self):
        if not self.attendance:
            return 0
        return (sum(self.attendance) / len(self.attendance)) * 100

    def __str__(self):
        percentage = self.calculate_attendance_percentage()
        return f"ID: {self.employee_id}, Name: {self.name}, Attendance: {percentage:.2f}%"

employees = []

def add_employee():
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    organization = input("Enter organization: ")
    employee = Employee(employee_id, name, organization)
    employees.append(employee)
    print("Employee added successfully!")

def mark_attendance():
    employee_id = input("Enter employee ID to mark attendance: ")
    for employee in employees:
        if employee.employee_id == employee_id:
            present = input("Is the employee present? (yes/no): ").lower() == "yes"
            employee.mark_attendance(present)
            print("Attendance marked!")
            return
    print("Employee not found!")

def display_employees():
    if employees:
        print("\nEmployee Attendance Records:")
        for employee in employees:
            print(employee)
    else:
        print("No employee records found!")

def attendance_menu():
    while True:
        print("\nEmployee Attendance Tracker")
        print("1. Add Employee")
        print("2. Mark Attendance")
        print("3. Display Employees")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            display_employees()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    attendance_menu()
