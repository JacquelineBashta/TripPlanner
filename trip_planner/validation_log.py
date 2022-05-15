""" 
This is a comment
"""
import logging



class ValidationLog:
    """ 
    This is a comment
    """
    
    def validation_log(data:str):
        """ 
        This is a comment
        """
        
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
        
        
    def validation_log2(self,data:str):
        """ 
        This is a comment
        """
        
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