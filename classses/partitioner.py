


class Partitioner:
    def __init__(self,hosts:list):
        self.hosts = hosts
        self.len = len(self.hosts)
        
    def message(self,message):
        raise NotImplemented("Please implement the accept message function")
        
        