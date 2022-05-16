
class ViewData:
    def __init__(self):
        # View Data ( expected to be filled with objects of type ttk.Entry or similar)
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

    def set_view_data_objects(self,objects):
        self.From_Location       = objects[0]
        self.From_Date           = objects[1]
        self.From_Time           = objects[2]
        self.To_Location         = objects[3]
        self.To_Date             = objects[4]
        self.To_Time             = objects[5]
        self.By_MeansOfTransport = objects[6]
        self.By_LinkForOffer     = objects[7]
        self.By_Cost             = objects[8]
        self.Stay_Where          = objects[9]
        self.Stay_LinkForOffer   = objects[10]
        self.Stay_Cost           = objects[11]
        self.Misc_Weather        = objects[12]
        self.Misc_Currency       = objects[13]
        self.Misc_MobileData     = objects[14]
        self.Notes               = objects[15]

    def set_view_data_value(self, attribute, value):
        if attribute == "Notes":
            self.Notes.delete(0,'end')
            self.Notes.insert(0, value)

        #elif hasattr(self,attribute):
        #    setattr(self,attribute,value)

        else:
            print(f"unsupported attribute name {attribute} !")



    def get_view_data_values(self):
        #TODO use the following implementation later
        value = []*16
        value_obj_lst = vars(self).values()
        for value_obj in value_obj_lst:
            val = value_obj.get()
            value.append(val)
        # value = [""]*16
        # value[0] = self.From_Location.get()
        # value[1] = self.From_Date.get()
        # value[2] = self.From_Time.get()
        # value[3] = self.To_Location.get()
        # value[4] = self.To_Date.get()
        # value[5] = self.To_Time.get()
        # value[6] = self.By_MeansOfTransport.get()
        # value[7] = self.By_LinkForOffer.get()
        # value[8] = self.By_Cost.get()
        # value[9] = self.Stay_Where.get()
        # value[10] = self.Stay_LinkForOffer.get()
        # value[11] = self.Stay_Cost.get()
        # value[12] = self.Misc_Weather.get()
        # value[13] = self.Misc_Currency.get()
        # value[14] = self.Misc_MobileData.get()
        # value[15] = self.Notes.get()
        return value

    def get_view_data_value(self, attribute):
        if attribute == "Notes":
            value = self.Notes.get()

        # elif hasattr(self,attribute):
        #     value = getattr(self,attribute)
            ret =  value

        else:
            print(f"unsupported attribute name {attribute} !")
            ret = ""

        return ret