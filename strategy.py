import pandas as pd
import indicators
import configparser
from sortedcontainers import SortedDict
from orderClass import Order
from strategy_arb import Strategy_arb
from strategy_mm import Strategy_MM
import pdb

def strategy(data, strategies):
    
    orders = []
    
    for strat in strategies:
        orders.extend(strat.run(data))
    
    return orders