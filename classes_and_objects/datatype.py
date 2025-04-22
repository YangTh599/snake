
class String():

    def __init__(self, val:str):
        self.val = val

    def change_string(self, new_str:str):
        self.val = new_str

class Integer():

    def __init__(self,val:int):
        self.val = int
    
    def change_int(self, new_int:int):
        self.val = new_int

class Float():

    def __init__(self, val:float):
        self.val = float

    def change_float(self, new_float:float):
        self.val = new_float

class Boolean():

    def __init__(self, val:bool):
        self.val = val

    def change_boolean(self):
        self.val = (not self.val)
    
    def change_true(self):
        self.val = True

    def change_false(self):
        self.val = False
        
