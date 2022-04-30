
import tkinter as tk
from datetime import datetime

class RowEntry:
         def __init__(self,row:dict):     
            self.Set_Defaults()      
           
            self.From_Location = row["From_Location"].get()
            self.From_Date = row["From_Date"].get()
            self.From_Time = row["From_Time"].get()
            self.To_Location = row["To_Location"].get()
            self.To_Date = row["To_Date"].get()
            self.To_Time = row["To_Time"].get()
            self.By_MeansOfTransport = row["By_MeansOfTransport"].get()
            self.By_LinkForOffer = row["By_LinkForOffer"].get()
            self.By_Cost = row["By_Cost"].get()
            self.Stay_Where = row["Stay_Where"].get()
            self.Stay_LinkForOffer = row["Stay_LinkForOffer"].get()
            self.Stay_Cost = row["Stay_Cost"].get()
            self.Misc_Weather = row["Misc_Weather"].get()
            self.Misc_Currency = row["Misc_Currency"].get()
            self.Misc_MobileData = row["Misc_MobileData"].get()           

         def Set_Defaults(self):
            self.From_Location = ""
            self.From_Date = ""
            self.From_Time = ""
            self.To_Location = ""
            self.To_Date = ""
            self.To_Time = ""
            self.By_MeansOfTransport = ""
            self.By_LinkForOffer = ""
            self.By_Cost = ""
            self.Stay_Where = ""
            self.Stay_LinkForOffer = ""
            self.Stay_Cost = ""
            self.Misc_Weather = ""
            self.Misc_Currency = ""
            self.Misc_MobileData = ""  

         def Get_To_Time(self):     
            return datetime(hour=int(self.To_Time.split(":")[0]), minute=int(self.To_Time.split(":")[1]) ,year=2022,month=1,day=1)
                            
         def Get_From_Time(self):
            return datetime(hour=int(self.From_Time.split(":")[0]), minute=int(self.From_Time.split(":")[1]) ,year=2022,month=1,day=1)
             