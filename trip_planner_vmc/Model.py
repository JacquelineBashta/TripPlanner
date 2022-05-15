import re

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

class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')
            
