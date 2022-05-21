
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


    def set_all_model_data(self, value):

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



    def get_all_model_data(self): 

        value_obj_lst = list(vars(self).values())
        return value_obj_lst
