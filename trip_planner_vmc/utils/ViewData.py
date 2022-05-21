
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

    def init_view_data_object(self, attribute,object):
        setattr(self,attribute, object)


    def set_all_view_data(self, value):
        i = 0
        for view_data_obj in vars(self).values():
            view_data_obj.delete(0,'end')
            view_data_obj.insert(0, value[i])
            i +=1
            
        
        
    def set_view_data_value(self, attribute, value):
        if attribute == "Notes":
            self.Notes.delete(0,'end')
            self.Notes.insert(0, value)
        else:
            print(f"unsupported attribute name {attribute} !")


    def get_view_data_value(self, attribute):
        if attribute == "Notes":
            value = self.Notes.get()
            ret =  value
        else:
            print(f"unsupported attribute name {attribute} !")
            ret = ""

        return ret


    def get_all_view_data_value(self):
        value = []*16
        value_obj_lst = vars(self).values()
        for value_obj in value_obj_lst:
            val = value_obj.get()
            value.append(val)
        return value


