import configparser

config=configparser.ConfigParser()
config.read('dbconfig.conf')

db='TESTDB'
host=config[db]['host']
print(host)