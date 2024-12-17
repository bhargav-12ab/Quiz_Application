# Quiz_Application

**Overview** - The Quiz Application is an interactive program designed to provide a dynamic quiz experience. The application is developed using Python for the backend logic and MariaDB as the database for storing user details securely. The application reads quiz questions from an Excel (XLSX) file, automatically jumbles the questions for every user to ensure uniqueness, and securely stores user information in a cryptographic format. The project also features a user-friendly interface for a seamless user experience.

**Key Features**
1. Dynamic Question Randomization: Questions are jumbled automatically for each user to ensure fairness and uniqueness.
2. Secure User Data Storage: User details are stored securely in the MariaDB database using cryptographic techniques.
3. Excel Integration: Quiz questions are imported from an external XLSX file for ease of management.
4. User-Friendly Interface: Designed with a simple and intuitive UI to provide a smooth experience for users.
5. Real-Time Performance Recording: User quiz scores and details are updated in the database instantly.

**Technology Stack**
1. Programming Language: Python
2. Database: MariaDB
3. Data Input: XLSX file (Excel) for quiz questions
4. Security: Cryptographic storage for user information

**Libraries/Tools**
1. pandas (for handling Excel files)
2. cryptography (for secure data storage)
3. mysql.connector (for connecting Python to MariaDB)
4. tkinter (for building the user-friendly interface)

**How It Works**
1. Loading Questions: The application loads questions from an Excel (XLSX) file using pandas.The questions are randomized for each user automatically.
2. User Authentication: User details such as name, email, and score are collected. These details are encrypted using cryptographic methods before being stored in the MariaDB database.
3. Quiz Flow:Users answer multiple-choice or descriptive questions displayed in a user-friendly graphical interface (built using tkinter).At the end of the quiz, scores are calculated and stored securely in the database.
4. Database Interaction: The MariaDB database stores user details, encrypted information, and quiz scores.
