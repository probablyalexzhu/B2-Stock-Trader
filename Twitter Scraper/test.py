import configparser 

#read configs API key with configparser
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['hello']['api_key']
