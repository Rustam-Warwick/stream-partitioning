import pandas as pd
from classses.partitioner import Partitioner
from classses.host import Host
from classses.streamer import Streamer
from partitioners.NeighborhoodPartition import NeighborhoodPartitioner

def main(filename):
    dataset = pd.read_csv(filename,sep='\t',usecols=[0,1])
    streamer  = Streamer(dataset=dataset,N=5)
    partitioner = NeighborhoodPartitioner([Host(i) for i in range(5)])
    streamer.subscribe(partitioner)
    streamer.run()
    
if __name__=="__main__":
    main("datasets/amazon0302_adj.tsv")
     