import logging

class ValidationLog:
    
    def validation_log(data:str):
        #create a logger
        logger = logging.getLogger('mylogger')
        logger.setLevel(logging.ERROR)
        handler = logging.FileHandler('mylog.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        #set filter to log only ERROR lines
        logger.addHandler(handler)
        
        logger.error(data)
        
        print("ERROR - " + data)
