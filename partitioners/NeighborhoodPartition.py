from classses.partitioner import Partitioner


class NeighborhoodPartitioner(Partitioner):
    def __init__(self,hosts):
        super().__init__(hosts)
        self.neigh = [dict() for _ in range(self.len)]
        
    
    
    def message(self,message):
        source, target = message
        chosenOne = 0
        
        for i in range(self.len):
            for j in range(self.len):
                sourceNeigh = self.neigh[i][source]
                destNeigh = self.neigh[i][target]
                
                
                
        self.neigh[chosenOne]['source'] = 1
        
        
        
        
        