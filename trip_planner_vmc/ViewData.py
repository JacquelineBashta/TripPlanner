from multiprocessing.dummy import Array


class ViewData:
    def __init__(self):
        # View Data
        self.From_Location       = None
        self.From_Date           = None
        self.From_Time           = None
        self.To_Location         = None
        self.To_Date             = None
        self.To_Time             = None
        self.By_MeansOfTransport = None
        self.By_LinkForOffer     = None
        self.By_Cost             = None
        self.Stay_Where          = None
        self.Stay_LinkForOffer   = None
        self.Stay_Cost           = None
        self.Misc_Weather        = None
        self.Misc_Currency       = None
        self.Misc_MobileData     = None
        self.Notes               = None


    def get_view_data(self,attribute)-> Array:
        if attribute == "ALL":
            values = [None]*16
            values[0] = self.From_Location.get()        
            values[1] = self.From_Date.get()             
            values[2] = self.From_Time.get()             
            values[3] = self.To_Location.get()           
            values[4] = self.To_Date.get()              
            values[5] = self.To_Time.get()              
            values[6] = self.By_MeansOfTransport.get()  
            values[7] = self.By_LinkForOffer.get()      
            values[8] = self.By_Cost.get()              
            values[9] = self.Stay_Where.get()           
            values[10] = self.Stay_LinkForOffer.get()    
            values[11] = self.Stay_Cost.get()            
            values[12] = self.Misc_Weather.get()         
            values[13] = self.Misc_Currency.get()        
            values[14] = self.Misc_MobileData.get()      
            values[15] = self.Notes.get()   
            return values

    def set_view_data(self,attribute, value):
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
