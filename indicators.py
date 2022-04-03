import pdb
def get_ltt(data, instrument_id):
    tradeticks = data[instrument_id]['tradeticks']
    if(len(tradeticks)==0):
        return None, None
    
    return tradeticks[-1].timestamp 


def get_best_bidask(data, instrument_id):
    bids = data[instrument_id]['orderbook'].bids
    asks = data[instrument_id]['orderbook'].asks
    
    return bids[0].price, asks[0].price

def get_cvwap(data, instrument_id):
    
    bids = data[instrument_id]['orderbook'].bids
    asks = data[instrument_id]['orderbook'].asks
    sumvp = 0
    sumv = 0
    
    for bid in bids:
        if(abs(bid.price - bids[0].price) > bids[0].price/10 ):
            break
        sumvp += bid.price*bid.volume
        sumv += bid.volume
        
    for ask in asks:
        if(abs(ask.price - asks[0].price) > asks[0].price/10 ):
            break
        sumvp += ask.price*ask.volume
        sumv += ask.volume
    # print(sumvp, sumv, sumvp/sumv)
    return (sumvp)/sumv