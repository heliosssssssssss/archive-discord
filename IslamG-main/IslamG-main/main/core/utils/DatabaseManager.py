import sqlite3

class DatabaseManager: 

    global conn
    conn = sqlite3.connect(r'main/IslamG/main/core/secure/data/userStats.db')

    global cursor
    cursor = conn.cursor()

    def FetchAllData():
        cursor.execute('SELECT * from islamQuiz')
        return cursor.fetchall()
    
    def getPointsFromUserID(userid):
        cursor.execute(f"SELECT * from islamQuiz WHERE userid = {int(userid)}")
        return cursor.fetchall()
    
    def createUser(userid):
        cursor.execute(f'INSERT into islamQuiz ("userid", "points") VALUES ({userid}, 0) ')
        conn.commit()

    def grantUser(userid, num):

        data = DatabaseManager.getPointsFromUserID(userid)
        actualNum = num + data[0][1]
        
        cursor.execute(f'UPDATE "islamQuiz" SET "points" = {int(actualNum)} WHERE "userid" = {userid}')
        conn.commit()

    def deductUser(userid, num):
        data = DatabaseManager.getPointsFromUserID(userid)
        actualNum = num - data[0][1]
        
        cursor.execute(f'UPDATE "islamQuiz" SET "points" = {int(actualNum)} WHERE "userid" = {userid}')
        conn.commit()

    def resetWARNDONOTUSE():
        cursor.execute(f'DELETE FROM islamQuiz')
        conn.commit()
