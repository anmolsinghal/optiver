from sortedcontainers import SortedDict, SortedList
import configparser
from orderClass import Order
import indicators
import pdb
config = configparser.ConfigParser()
config.read('CONFIG')

class Strategy_MM:
    
    def __init__(self, instrument):
        self.tolerance = float(config['STRATEGY']['cancellation_tolerance'])
        self.levels = [int(x) for x in config['STRATEGY']['levels'].split()]
        self.qty = float(config['STRATEGY']['level_volume'])
        self.existing_bids = []
        self.existing_asks = []
        self.instrument_id = instrument
        self.counter = 0
        
    def determineOrders(self,fairPrice):
        return ([round(fairPrice * (1+ x*0.0001) - 0.05,1) for x in self.levels ], [round(fairPrice * (1- x*0.0001) + 0.05,1) for x in self.levels ])
    
    
    def run(self,data):
        self.counter += 1
        fairPrice = indicators.get_cvwap(data, self.instrument_id)
        
        order_levels = self.determineOrders(fairPrice)
        
        orders = []
       
        for x in order_levels[0]:
            order = Order(2, self.instrument_id, x, self.qty, 'ask', 'limit')
            orders.append(order)
            
              
        for x in order_levels[1]:
            order = Order(2, self.instrument_id, x, self.qty, 'bid', 'limit')
            orders.append(order)
            
        return orders