# MySQL Database Backup

This script will backup your database and submit it to GitHub, on the assumption that your Github is set over SSH. 

The script has been build on python version 2.7.3 .

## Dependencies 
You are required to <b>install python</b> on your machine, also <b>install MySQLdb</b> module for python. 

## Structure

When the script will run it will create some folders as follows:

- One folder named backup
- Inside the folder backup it will be create a current day folder ie: 20150605
- Inside the current day folder it will be create a folder with each database which will contain an sql.gzip file 

##Configure

#### <b>Open</b> the file <b>osb_backup.py</b> to <b>edit</b>.

Change:
<code>

  <b>sqlHost = 'localhost';</b>
  
  <b>sqlUser = 'username';</b>
  
  <b>sqlPsw	= 'password';</b>

  <b>path = "/var/www"; <b/>
  
</code>
with your settings.

Save the file and you are done!

## Run it!

In the terminal type:<br/>
<code>./osb_backup.py</code>




