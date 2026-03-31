# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
use-case-diagram.png
### Flowchart of the main workflow
```mermaid
graph TD
    Start[Start Program] --> Init[Init Data: Load JSON or Seed Defaults]
    Init --> LoginMenu{Login Menu}
    
    LoginMenu -- "[1] Student Login" --> StudentID{ID Found or 'new'?}
    StudentID -- "new" --> CreateProfile[Create Student Profile]
    StudentID -- "ID exists" --> StudentMenu[Student Menu]
    CreateProfile --> StudentMenu
    
    StudentMenu --> SOptions{Student Options}
    SOptions -- "1-6: View/Reg/Drop/Bill/Edit" --> SAction[Perform Action]
    SAction --> StudentMenu
    SOptions -- "7: Logout" --> SaveS[Save Data]
    SaveS --> LoginMenu
    
    LoginMenu -- "[2] Admin Login" --> AdminPass{Correct Password?}
    AdminPass -- "Yes" --> AdminMenu[Admin Menu]
    AdminPass -- "No" --> LoginMenu
    
    AdminMenu --> AOptions{Admin Options}
    AOptions -- "1-9: Manage Courses/Students" --> AAction[Perform Action]
    AAction --> AdminMenu
    AOptions -- "10: Logout" --> SaveA[Save Data]
    SaveA --> LoginMenu
    
    LoginMenu -- "[3] Exit" --> FinalSave[Final Save & Exit]
```
### Prompts

- "To help you complete Task 1, I need to see the core logic of the application."
- "Analyze the provided Main.java and EnrollmentSystem.java to identify the core business logic."
- "Select the 'Billing Summary' use case and reengineer the calculateTuition method from Java into an equivalent Python script."
- "Ensure the improve Python version uses a class structure and handles missing student/course data similarly to the original Java logic."
