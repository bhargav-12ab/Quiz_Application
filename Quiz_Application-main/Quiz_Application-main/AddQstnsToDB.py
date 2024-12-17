import openpyxl
import pymysql.cursors  

# Load Excel file
loc = "/home/abhiram/Downloads/Quiz Application Using MYSQL/Resources/Questions.xlsx"
wb = openpyxl.load_workbook(loc)
sheet = wb.active

# Connect to database  
conn = pymysql.connect(host='localhost',
                       database='world', 
                       user='root',
                       password='root',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

# Check if table exists, drop if so
cursor.execute("SHOW TABLES LIKE 'questions'")
if cursor.fetchone() is not None:
  print("Table exists, dropping...")
  cursor.execute("DROP TABLE IF EXISTS questions")

# Create table
cursor.execute("""
  CREATE TABLE questions (
    QID INT,
    qstn VARCHAR(255),  
    opA VARCHAR(255),
    opB VARCHAR(255),
    opC VARCHAR(255),
    opD VARCHAR(255), 
    ans INT)  
""")

# Insert data from Excel 
header = True
for row in sheet.values:
  if header:
    # Skip header row
    header = False
    continue

  qid = int(row[0])
  
  if not isinstance(qid, int):
    raise ValueError("QID must be integer")
    
  # Insert question text and options
  cursor.execute("INSERT INTO questions (qstn, opA, opB, opC, opD,ans) VALUES (%s, %s, %s, %s, %s,%s)", tuple(row[1:7]))
  
  # Update QID 
  cursor.execute("UPDATE questions SET QID = %s WHERE qstn = %s", (qid, row[1]))  

conn.commit()

cursor.close()  
conn.close()
