from orderClass import Order
import indicators
import configparser
config = configparser.ConfigParser()
config.read('CONFIG')
class Strategy_arb:
    
    def __init__(self):
        self.arbmin = float(config['STRATEGY']['arbmin'])
        self.instrument_ids = config['GENERAL']['instrument_ids'].split()
        
    
    def check_stat_arb(self, data, instrument_ids):
    
        bbid_a, bask_a = indicators.get_best_bidask(data, instrument_ids[0])
        bbid_b, bask_b = indicators.get_best_bidask(data, instrument_ids[1])
        
        if(bbid_b - bask_a > self.arbmin ):
            return 1
        
        if( bbid_a - bask_b > self.arbmin):
            return -1
        
        return 0


    def arbtrading(self, data, instrument_ids, mode):
        
        orders = []
        
        if(mode == 1):
            buy_instrument = instrument_ids[0]
            sell_instrument = instrument_ids[1]
        else:
            buy_instrument = instrument_ids[1]
            sell_instrument = instrument_ids[0]
            
        bids = data[sell_instrument].bids
        asks = data[buy_instrument].asks
        
        levelbid = 0
        qtyb = 0
        qtya = 0
        
        while(levelbid < len(bids) and bids[levelbid].price - asks[0].price > self.arbmin):
            qtyb += bids[levelbid].volume
            levelbid += 1
        levelask = 0
        
        while(levelask < len(asks) and bids[0].price - asks[levelask].price > self.arbmin):
            qtya += asks[levelask].volume
            levelask += 1
        
        qty = min(qtyb, qtya)
        buy_order = Order(1, buy_instrument, asks[0].price, qty, 'bid', 'limit')
        sell_order = Order(1, sell_instrument, asks[0].price, qty,'ask', 'limit')
        
        orders.append(buy_order)
        orders.append(sell_order)
        
        return orders
    
    def run(self, data):
        orders = []
        arb = self.check_stat_arb(data, self.instrument_ids)
    
        if(arb != 0):
            orders.extend(self.arbtrading(data, self.instrument_ids, arb))
        
        return orders