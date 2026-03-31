# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram

graph TD
    A[Start] --> B[Init Data & Load JSON]
    B --> C{Login Menu}
    C -->|Option 1| D[Student Login]
    C -->|Option 2| E[Admin Login]
    C -->|Option 3| F[Save & Exit]
    
    D --> G{Student ID found?}
    G -->|No/ 'new'| H[Create New Profile]
    G -->|Yes| I[Student Menu]
    H --> I
    
    I --> J{Student Options}
    J -->|1-6| K[View/Register/Drop/Schedule/Billing/Edit]
    J -->|7| L[Logout & Save]
    L --> C

    E --> M{Password Correct?}
    M -->|Yes| N[Admin Menu]
    M -->|No| C
    
    N --> O{Admin Options}
    O -->|1-9| P[Manage Courses/Students/Rosters/Billing]
    O -->|10| Q[Logout & Save]
    Q --> C

### Flowchart of the main workflow

### Prompts
