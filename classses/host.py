from typing import Set

class Host:
    
    def __init__(self,index=0,memory=1000):
        self.index = index # Index of the host 
        self.memory  = memory # Memory limit in number of accepted entries
        self.data = set() # Accepted Data
    
    def addToPartition(self,data):
        self.data.add(data)
    