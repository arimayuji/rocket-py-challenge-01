class Contact:
    def __init__(self,name:str,phone:str,email:str):
        self.name = name
        self.phone = phone
        self.email = email
        self.is_favorite = False
    def __str__(self):
        return f"{self.name} : {self.phone}"