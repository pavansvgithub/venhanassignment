import sqlite3 

def insert_student(name,grade):
    conn = sqlite3.connect("students.db") 
    cursor = conn.cursor()
    cursor.execute("""
     INSERT INTO students(name,grade)
                   VALUES(? , ?)
                   """,(name,grade)) 
    
    conn.commit()

    conn.close()

insert_student("Alice",80.0)