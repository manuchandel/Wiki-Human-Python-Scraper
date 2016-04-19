import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="", db="TestData",charset='utf8' )
cursor=db.cursor()

sql="""CREATE TABLE IF NOT EXISTS WikiHumans (
  ID INT(11) NOT NULL AUTO_INCREMENT,
  NAME VARCHAR(100) DEFAULT NULL,
  DESCRIPTION VARCHAR(200),
  PRIMARY KEY (ID)
) ENGINE=InnoDB"""

cursor.execute(sql)
cursor.close()
