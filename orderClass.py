from collections import defaultdict
class Order:
    def __init__(self, strategy: int, instrument_id: str, price: float, volume: int, side: str, order_type: str):
        self.strategy: int = strategy # 1 or 2 
        self.instrument_id: str = instrument_id # 'PHILIPS_A' or 'PHILIPS_B'
        self.price: float = price # Is a float
        self.volume: int = volume # Is volume
        self.side: str = side # Is either 'ask' or 'bid'
        self.order_type = order_type # Is 'limit'
        
    def __str__(self):
        # return str(self.strategy)+", " + str(self.instrument_id)+", "  + str(self.price)+", "  + str(self.volume)+", " +self.side
        return f'{str(self.strategy)},{self.instrument_id},{str(self.price)},{str(self.volume)},{self.side}'
        
        

        
 
            
    
            
            
    
    
    
        
        
    
            
        