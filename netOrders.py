from collections import defaultdict
import pdb

def compressOrders(data, orders, instrument_ids):
    # print([[str(x.strategy),x.instrument_id,str(x.price),(str(x.volume)),x.side] for x in orders])
    outstanding_orders =  {instrument_id:get_outstanding_orders(data, instrument_id ) for instrument_id in instrument_ids}
    intermediateOrders = agreggateOrder(orders)
    
    actions, keep_orders = revisedOrderBook(outstanding_orders,intermediateOrders, instrument_ids)
    
    for instrument_id in instrument_ids:
        orders = data[instrument_id]['outstanding']
        
        for x in orders:
            if(orders[x] not in keep_orders):
                actions.append(('C', 0,orders[x]))
    
    return actions
    
def get_outstanding_orders(data, instrument_id ):
    orders = data[instrument_id]['outstanding']
    bids = dict()
    asks = dict()
    # print(orders)
    for  x in orders:
        if(orders[x].side == "bid"):
            if(bids.get(orders[x].price)):
                bids[orders[x].price].append(orders[x])
            else:
                bids[orders[x].price] = [orders[x]]
        else:
            if(asks.get(orders[x].price)):
                asks[orders[x].price].append(orders[x])
            else:
                asks[orders[x].price] = [orders[x]]
    
    return {"bids":bids,"asks":asks}


def agreggateOrder(orderList):
        
        netOrders = defaultdict(list)
        for x in orderList:
            if(not netOrders.get((x.instrument_id,x.price))):
                netOrders[(x.instrument_id,x.price)].append(x)
            else:
                
                y = netOrders.get((x.instrument_id,x.price))[0]
                if (y.side == x.side):
                    y.volume += x.volume
                else:
                    if(y.side < x.side):
                        y.side = x.side
                        y.volume = x.volume-y.volume
                    else:
                        y.volume -= x.volume
        
        return netOrders

def revisedOrderBook(outstanding_orders,netOrders, instrument_ids):
    # instrument_ids = config['GENERAL']['instrument_ids'].split()
    
    newOrders = []
    keep_orders = []
    for l in netOrders:
        
        newOrd = netOrders[l][0]
        # pdb.set_trace()
        ins,price = l
        bid,ask = outstanding_orders[ins]['bids'],outstanding_orders[ins]['asks']
        
        if(bid.get(price)):
            existing = bid.get(price)[0]
            if(newOrd.side == 'ask'):
                if(newOrd.volume == existing.volume):
                    newOrders.append(('C', 0,existing))
                elif(newOrd.volume > existing.volume):
                    newOrders.append(('C', 0,existing))
                    newOrders.append(('A',newOrd.volume-existing.volume,newOrd))
                else:
                    newOrders.append(('M',existing.volume - newOrd.volume ,existing))
                    keep_orders.append(existing)
            else:
                newOrders.append(('M',newOrd.volume ,existing))
                keep_orders.append(existing)
        
        elif(ask.get(price)):
            existing = ask.get(price)[0]
            
            if(newOrd.side == 'bid'):
                if(newOrd.volume == existing.volume):
                    newOrders.append(('C', 0,existing))
                elif(newOrd.volume > existing.volume):
                    newOrders.append(('C', 0,existing))
                    newOrders.append(('A',newOrd.volume-existing.volume,newOrd))
                else:
                    newOrders.append(('M',existing.volume - newOrd.volume ,existing))
                    keep_orders.append(existing)
            else:
                newOrders.append(('M',newOrd.volume ,existing))
                keep_orders.append(existing)
                    
        else:
            newOrders.append(('A',newOrd.volume,newOrd))
            
        
        # if(bid.get(price)):
        #     existing = bid.get(price)[0]
        #     if(newOrd.side == "bid"):
        #       newOrders.append(('M',newOrd.volume+ existing.volume,existing)) 
        #     elif(existing.volume > newOrd.volume):
        #         newOrders.append(('M',newOrd.volume - existing.volume,existing)) 
        #     elif(existing.volume == newOrd.volume):
        #         newOrders.append(('C', 0,existing)) 
        #     else:
        #         newOrders.append(('C', 0,existing)) 
        #         newOrders.append(('A',newOrd.volume-existing.volume,newOrd)) 
                
        # elif(ask.get(price)):
        #     existing = ask.get(price)[0]
        #     if(newOrd.side == "ask"):
        #       newOrders.append(('M',newOrd.volume+ existing.volume,existing)) 
        #     elif(existing.volume > newOrd.volume):
        #         newOrders.append(('M',newOrd.volume - existing.volume,existing)) 
        #     elif(existing.volume == newOrd.volume):
        #         newOrders.append(('C', 0,existing)) 
        #     else:
        #         newOrders.append(('C', 0,existing)) 
        #         newOrders.append(('A',newOrd.volume-existing.volume,newOrd)) 
        # else:
        #     newOrders.append(('A',newOrd.volume,newOrd))
    return newOrders, keep_orders