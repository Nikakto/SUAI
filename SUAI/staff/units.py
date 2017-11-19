class Unit():
    
    name = ''
    short_name = ''
    meters = 1;
    
    def __init__(self, name, shortname, meters):
        self.name = name
        self.shortname = shortname
        self.meters = meters
        
    def convert(self, to_unit):
        return 1