from optibook.synchronous_client import Exchange
import strategy
import pandas as pd
import configparser
import logging
from poll_data import read_data
from place_orders import LOB
from orderClass import Order
import time
from netOrders import compressOrders
from strategy_arb import Strategy_arb
from strategy_mm import Strategy_MM
import pdb
logger = logging.getLogger('client')
logger.setLevel('ERROR')

print("Setup was successful.")

e = Exchange()


a = e.connect()


config = configparser.ConfigParser()
config.read('CONFIG')

order_placer = LOB()

instrument_ids = config['GENERAL']['instrument_ids'].split()
mmstrat0 = Strategy_MM(instrument_ids[0])
arbstrat = Strategy_arb()
mmstrat1 = Strategy_MM(instrument_ids[1])
   
strategies = [mmstrat0, mmstrat1]
    
for s, p in e.get_positions().items():
    if p > 0:
        e.insert_order(s, price=1, volume=p, side='ask', order_type='ioc')
    elif p < 0:
        e.insert_order(s, price=100000, volume=-p, side='bid', order_type='ioc')      
    
while(e.is_connected()):
    delay = 1/int(config['GENERAL']['tickspeed'])
    time.sleep(delay)
    
    data, positions, pnl = read_data(e,instrument_ids )
    orders = strategy.strategy(data, strategies)
    
    orders = compressOrders(data, orders,config['GENERAL']['instrument_ids'].split() )
    order_placer.updateList(e, orders)
    # pdb.set_trace()