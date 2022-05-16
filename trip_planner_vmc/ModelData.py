
#TODO check if import is correct
from multiprocessing.dummy import Array


class ModelData:
    def __init__(self):
        # Model Data
        self.From_Location       = ""
        self.From_Date           = ""
        self.From_Time           = ""
        self.To_Location         = ""
        self.To_Date             = ""
        self.To_Time             = ""
        self.By_MeansOfTransport = ""
        self.By_LinkForOffer     = ""
        self.By_Cost             = ""
        self.Stay_Where          = ""
        self.Stay_LinkForOffer   = ""
        self.Stay_Cost           = ""
        self.Misc_Weather        = ""
        self.Misc_Currency       = ""
        self.Misc_MobileData     = ""
        self.Notes               = ""

    def get_model_data(self,attribute)-> Array:
        if attribute == "ALL":
            values = [""]*16
            values[0] = self.From_Location     
            values[1] = self.From_Date             
            values[2] = self.From_Time             
            values[3] = self.To_Location           
            values[4] = self.To_Date              
            values[5] = self.To_Time              
            values[6] = self.By_MeansOfTransport  
            values[7] = self.By_LinkForOffer      
            values[8] = self.By_Cost              
            values[9] = self.Stay_Where           
            values[10] = self.Stay_LinkForOffer    
            values[11] = self.Stay_Cost            
            values[12] = self.Misc_Weather         
            values[13] = self.Misc_Currency        
            values[14] = self.Misc_MobileData      
            values[15] = self.Notes   
            return values

    def set_model_data(self,attribute, value):
        if attribute == "ALL":
            self.From_Location       = value[0]
            self.From_Date           = value[1]
            self.From_Time           = value[2]
            self.To_Location         = value[3]
            self.To_Date             = value[4]
            self.To_Time             = value[5]
            self.By_MeansOfTransport = value[6]
            self.By_LinkForOffer     = value[7]
            self.By_Cost             = value[8]
            self.Stay_Where          = value[9]
            self.Stay_LinkForOffer   = value[10]
            self.Stay_Cost           = value[11]
            self.Misc_Weather        = value[12]
            self.Misc_Currency       = value[13]
            self.Misc_MobileData     = value[14]
            self.Notes               = value[15]

















