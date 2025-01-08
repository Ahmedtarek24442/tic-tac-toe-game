class players:
    def __init__(self, name, sympol):
        self.name = name
        self.sympol = sympol.upper()
        self.score = 0
    
    def get_sympol(self):
        return self.sympol
    
    def getname_name(self):
        return self.name
    
    def get_score(self):
        return self.score