# python/billing_system.py

class BillingSystem:
    """
    Reengineered Python version of the EnrollmentSystem's 
    tuition calculation logic.
    """
    TUITION_PER_CREDIT = 300.0

    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_sample_data(self):
        self.students["S101"] = {"name": "Alice", "enrolled_courses": ["CS101", "MATH201"]}
        self.courses["CS101"] = {"title": "Intro to CS", "credits": 4}
        self.courses["MATH201"] = {"title": "Calculus II", "credits": 3}

    def calculate_tuition(self, student_id):
        """
        Calculates the total tuition for a student based on enrolled credits.
        Equivalent to EnrollmentSystem.calculateTuition() in Java.
        """
        student = self.students.get(student_id)
        if not student:
            return -1.0
        
        total_credits = 0
        for code in student["enrolled_courses"]:
            course = self.courses.get(code)
            if course:
                total_credits += course["credits"]
        
        return total_credits * self.TUITION_PER_CREDIT

#Example Usage
if __name__ == "__main__":
    billing = BillingSystem()
    billing.add_sample_data()
    
    student_id = "S101"
    total = billing.calculate_tuition(student_id)
    
    if total != -1.0:
        print(f"--- Billing Summary for {student_id} ---")
        print(f"Total Tuition: ${total:,.2f}")
    else:
        print("Student not found.")
