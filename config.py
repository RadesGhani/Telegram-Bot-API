#this is the basic configuration file for main.py
#for database configuration, look for the bottom of the file

#telegram bot configuration
class teleConfig :
    botToken    = "[TELEGRAM BOT TOKEN]"   #Telegram Bot Token obtained from BotFather
    api         = "http://127.0.0.1:5002"                           #Flask api url

#flask configuration
class flaskConfig :
    port        = '5002'

#Bellow is the database configuration
#Engine is the database server, for a list of available engine refers to https://docs.sqlalchemy.org/en/13/core/engines.html
class dbConfig :
    dialect     = "oracle"
    sql_driver  = "cx_oracle"
    user        = "[ORACLEDB_USER]"
    password    = "[ORACLEDB_PASSWORD]"
    url         = "[ORACLEDB_URL]"
    port        = "[ORACLEDB_PORT]"
    service_name= "orcl.dba"