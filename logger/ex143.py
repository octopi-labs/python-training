import logging

#Create and configure logger 
logging.basicConfig(filename="system_log_2.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='a') 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("This is exception logging.")