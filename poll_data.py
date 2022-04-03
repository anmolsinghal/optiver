from optibook.synchronous_client import Exchange
import pandas as pd

import logging
from collections import defaultdict
import pdb

def read_data(e,instrument_ids):
    data = defaultdict(dict)
    positions = e.get_positions()
    pnl = e.get_pnl()
    for instrument_id  in instrument_ids:
       
        book = e.get_last_price_book(instrument_id)
        data[instrument_id]['orderbook'] = book
        tradeticks = e.poll_new_trade_ticks(instrument_id)
        
        data[instrument_id]['tradeticks'] = tradeticks
        # for t in tradeticks:
        #     print(f"[{t.instrument_id}] price({t.price}), volume({t.volume}), aggressor_side({t.aggressor_side}), buyer({t.buyer}), seller({t.seller})")
        
        # to read trade ticks since start of time
        # tradeticks = e.get_trade_tick_history(instrument_id)
        # for t in tradeticks:
        #     print(t)
        
        outstanding = e.get_outstanding_orders(instrument_id)
        data[instrument_id]['outstanding'] = outstanding
        for o in outstanding.values():
            print(f"Outstanding order: order_id({o.order_id}), instrument_id({o.instrument_id}), price({o.price}), volume({o.volume}), side({o.side})")
        
    
        trades = e.poll_new_trades(instrument_id)
        data[instrument_id]['trades'] = trades
        for t in trades:
            print(f"[TRADED {t.instrument_id}] price({t.price}), volume({t.volume}), side({t.side})")
        
    
    return data, positions, pnl