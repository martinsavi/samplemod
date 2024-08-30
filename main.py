import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd='1234',
    database="testdatabase"
    )

users  =[('tim', 'techtim'),
         ('joe', 'joeylul'),
         ('sarah', 'sara123')]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]

posts  =[(8,1, 'mamatcholas'),
         (8,2, 'aaaa'),
         (8,3, 'lmao'),
         (8,4, 'lybtsg'),
         (9,5, 'omegalul'),
         (10,6, 'sus')]

mycursor = db.cursor()

Q1 = "CREATE TABLE Users (id INT PRIMARY KEY  AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(50))"

Q2 = '''CREATE TABLE Scores 
    (userID int PRIMARY KEY, 
     FOREIGN KEY(userID) REFERENCES Users(id),
     game1 INT DEFAULT 0, 
     game2 INT DEFAULT 0)'''
    
Q2 = '''CREATE TABLE Posts
    (post INT PRIMARY KEY, 
     userID INT,
     FOREIGN KEY(userID) REFERENCES Users(id),
     content VARCHAR(50))'''
    
# mycursor.execute(Q1)
# mycursor.execute(Q2)
# db.commit()

# mycursor.execute("SHOW TABLES")

Q3 = "INSERT INTO Users (name, password) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (userID, game1, game2) VALUES (%s,%s,%s)"
Q5 = "INSERT INTO Posts (userID, post, content) VALUES (%s,%s,%s)"

mycursor.executemany(Q5, posts)

# for x, user in enumerate(users):
#     mycursor.execute(Q3, user)
#     last_id = mycursor.lastrowid
#     mycursor.execute(Q4, (last_id,)+user_scores[x])
# db.commit()

mycursor.execute("SELECT * FROM Posts")

for x in mycursor:
    print(x)
    
# mycursor.execute("SELECT * FROM Users")

# for x in mycursor:
#     print(x)