#!/usr/bin/env python
import MySQLdb
import os
import time
import subprocess

sqlHost = 'localhost';
sqlUser = 'username';
sqlPsw	= 'password';

backupDir = "backup";

now=time.strftime("%Y%m%d")


#create backup dir
if not (os.path.isdir(backupDir)):
  os.mkdir(backupDir)
print "Directory " + backupDir+ " created!"

#create todays folder
os.chdir(backupDir)

if not (os.path.isdir(now)):
  os.mkdir(now)
  print "Directory "+now+" created "

#enter today folder
os.chdir(now)


##DB SETUP
connection = MySQLdb.connect(
                host = sqlHost,
                user = sqlUser,
                passwd = sqlPsw) 

cursor = connection.cursor()    
cursor.execute("SHOW databases")  
tables = cursor.fetchall()
print "connection to database created"

##LOOP OVER DBs
for (table_name,) in cursor:
  table = table_name
  os.mkdir(table_name)
  os.chdir(table_name) 
  prc = subprocess.Popen("mysqldump -u"+sqlUser+" -p"+sqlPsw+"  "+table+" | gzip > "+table+".sql.gzip ",shell=True)
  prc.wait()
  os.chdir("..")  
  print  table_name + " - is backed up"

subprocess.Popen("git add -A ",shell=True)
subprocess.Popen("git commit -m 'automatic backup'",shell=True)
subprocess.Popen("git push -f origin master",shell=True)
