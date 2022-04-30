
import tkinter as tk
from datetime import datetime
from ValidationLog import ValidationLog as VL

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

         def Get_To_DateTime(self):     
            return datetime(hour=int(self.To_Time.split(":")[0]), minute=int(self.To_Time.split(":")[1]), \
               day=int(self.To_Date.split("/")[0]),month=int(self.To_Date.split("/")[1]),year=int(self.To_Date.split("/")[2]))
                            
         def Get_From_DateTime(self):
            return datetime(hour=int(self.From_Time.split(":")[0]), minute=int(self.From_Time.split(":")[1]), \
               day=int(self.From_Date.split("/")[0]),month=int(self.From_Date.split("/")[1]),year=int(self.From_Date.split("/")[2]))
         
         def Is_valid_Cost(self,cost:str):
            return_cost = 0
            if cost.isdigit():
               return_cost = float(cost) 
            elif cost == "Cost" or cost == "":
               return_cost = 0
            else:
               VL.validation_log("Invalid Cost Value "+str(cost)+" , Please add value in Euro")
               return_cost = 0
            return return_cost   

         def Get_By_Cost(self):
            return self.Is_valid_Cost(self.By_Cost)

         def Get_Stay_Cost(self):
            return self.Is_valid_Cost(self.Stay_Cost) 
         
