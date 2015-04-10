

import pg8000


release = ""

cbo = 0
lcom = 0


conn = pg8000.connect(database="D3", host="localhost",user="sukhi",password="sukhi",port=5432)
cursor = conn.cursor()

def createTable():
    cursor.execute("CREATE SEQUENCE seq1")
    cursor.execute("CREATE TABLE T31(ID INT UNIQUE NOT NULL "
                   "DEFAULT NEXTVAL('FILE_id_seq'), RELEASE varchar(100) NOT NULL ,class_path varchar(250) , LCOM INT NOT NULL, CBO INT NOT NULL ) ")
    cursor.execute("CREATE TABLE T32(ID INT UNIQUE NOT NULL "
                   "DEFAULT NEXTVAL('FILE_id_seq'), RELEASE varchar(100) NOT NULL ,class_path varchar(250), LCOM INT NOT NULL, CBO INT NOT NULL ) ")
    cursor.execute("CREATE TABLE T33(ID INT UNIQUE NOT NULL "
                   "DEFAULT NEXTVAL('FILE_id_seq'), RELEASE varchar(100) NOT NULL ,class_path varchar(250) , LCOM INT NOT NULL, CBO INT NOT NULL ) ")
    cursor.execute("CREATE TABLE T34(ID INT UNIQUE NOT NULL "
                   "DEFAULT NEXTVAL('FILE_id_seq'), RELEASE varchar(100) NOT NULL ,class_path varchar(250) , LCOM INT NOT NULL, CBO INT NOT NULL ) ")
    conn.commit()
    return




def insert(release,class_path,lcom,cbo):
    cursor.execute("INSERT INTO T"+ release +"(RELEASE,class_path,LCOM,CBO) VALUES(%s,%s,%s,%s)",(release,class_path,lcom,cbo,))
    conn.commit()
    return


#createTable()

#SaveToDB(release,class_path, lcom,cbo)
