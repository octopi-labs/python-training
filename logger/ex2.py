import logging 

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'  
logging.basicConfig(filename="system_log_1.log", 
                    format=FORMAT, 
                    filemode='w')

d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}

#Creating an object 
logger=logging.getLogger("server") 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)

logger.warning('Protocol problem: %s', 'connection reset', extra=d)
