from multiprocessing import Pool 
from typing import Sequence
from classses.partitioner import Partitioner


class Streamer:
    def __init__(self,dataset,N=5):
        self.dataset = dataset
        self.N = N
        self.partitioners:Sequence[Partitioner] = list()
        
    def subscribe(self,partitioner:Partitioner):
        self.partitioners.append(partitioner)
        
    def run(self):
        def applyFunction(dataRow):
            for partitioner in self.partitioners:
                partitioner.message(dataRow)
        self.dataset.apply(applyFunction)
        # with Pool(processes=self.N) as p:
        #     p.map(applyFunction,self.dataset.values)
        
            
        
        
        