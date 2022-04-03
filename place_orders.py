from sortedcontainers import SortedDict
import time

class LOB:
    def __init__(self):
        self.totalPositionsPA = 0
        self.totalPositionsPB = 0
        self.orderTracker = dict()
        self.actionCount = 0
        self.timeEpoch = time.time()
        
        
    def updateList(self, e, orderTupleList):
        print("Epoch is " + str(self.timeEpoch))
        outstanding = e.get_outstanding_orders('PHILIPS_A')
        for o in outstanding.values():
            print(f"Outstanding order: order_id({o.order_id}), instrument_id({o.instrument_id}), price({o.price}), volume({o.volume}), side({o.side})")
        outstanding = e.get_outstanding_orders('PHILIPS_B')
        for o in outstanding.values():
            print(f"Outstanding order: order_id({o.order_id}), instrument_id({o.instrument_id}), price({o.price}), volume({o.volume}), side({o.side})")
            
        print("PreTuple is")
        
        for orderTuple in orderTupleList:
            charFlag = orderTuple[0]
            orderEle = orderTuple[2]
            if charFlag == 'C':
                print(charFlag, orderTuple[1], orderEle.instrument_id, orderEle.price, orderEle.volume, orderEle.side)
                self.deleteOrder(e, orderEle.instrument_id, orderEle.order_id)
        print("PostTuple is")
        
        outstanding = e.get_outstanding_orders('PHILIPS_A')
        for o in outstanding.values():
            print(f"Outstanding order: order_id({o.order_id}), instrument_id({o.instrument_id}), price({o.price}), volume({o.volume}), side({o.side})")
        outstanding = e.get_outstanding_orders('PHILIPS_B')
        for o in outstanding.values():
            print(f"Outstanding order: order_id({o.order_id}), instrument_id({o.instrument_id}), price({o.price}), volume({o.volume}), side({o.side})")
            
        
        for orderTuple in orderTupleList:
            charFlag = orderTuple[0]
            orderEle = orderTuple[2]
            if charFlag == 'A':
                print(charFlag, orderTuple[1], orderEle.instrument_id, orderEle.price, orderEle.volume, orderEle.side)
                self.addOrder(e, orderEle.strategy, orderEle.instrument_id, orderEle.price, orderEle.volume, orderEle.side, orderEle.order_type)
            elif charFlag == 'M':
                print(charFlag, orderTuple[1], orderEle.instrument_id, orderEle.price, orderEle.volume, orderEle.side)
                self.modifyOrder(e, orderEle.instrument_id, orderEle.order_id, orderTuple[1])
            

    def addOrderList(self, e, orderList):
        for orderEle in orderList:
            self.addOrder(e, orderEle.strategy, orderEle.instrument_id, orderEle.price, orderEle.volume, orderEle.side, orderEle.order_type)
        
    def addOrder(self, e, strategy: int, instrument_id: str, price: float, volume: int, side: str, order_type: str) -> int:
        self.timeHeat()
        order_id = e.insert_order(instrument_id, price=price, volume=volume, side=side, order_type=order_type)
        self.orderTracker[order_id] = (strategy, instrument_id, price, volume, side, order_type)
        return order_id
        
    def deleteOrder(self, e, instrument_id: str, order_id: int) -> bool:
        self.timeHeat()
        success = e.delete_order(instrument_id, order_id=order_id)
        if success:
            del self.orderTracker[order_id]
            return -1
        else:
            disorder = self.orderTracker[order_id]
            del self.orderTracker[order_id]
            if disorder == 'ask':
                return self.addOrder(e, disorder[0], disorder[1], disorder[2], disorder[3], 'bid', disorder[5])
            else:
                return self.addOrder(e, disorder[0], disorder[1], disorder[2], disorder[3], 'ask', disorder[5])
            
    def modifyOrder(self, e, instrument_id, order_id, volume):
        success = e.amend_order(instrument_id, order_id=order_id, volume=volume)
        if not success:
            currentOrder = self.orderTracker[order_id]
            diff = volume - currentOrder[3]
            if diff > 0:
                self.addOrder(e, currentOrder[0], currentOrder[1], currentOrder[2], diff, self.flipSwitch(currentOrder[4]), currentOrder[5])
            elif diff < 0:
                self.addOrder(e, currentOrder[0], currentOrder[1], currentOrder[2], diff, self.flipSwitch(currentOrder[4]), currentOrder[5])
            del self.orderTracker[order_id]
    
    def flipSwitch(self, strbool):
        if strbool == 'ask':
            return 'bid'
        else:
            return 'ask'
    
    def hedgeAlarm(self):
        sumPos = self.totalPositionsPA + self.totalPositionsPB
        if abs(sumPos) > 40:
            return True
        return False
        
    def timeHeat(self) -> bool:
        if self.actionCount <= 25:
            self.actionCount +=1
            return True
        else:
            if time.time() - self.timeEpoch >= 1:
                self.timeEpoch = time.time()
                self.actionCount = 0
                return True
            else:
                time.sleep(max(1 - (time.time() - self.timeEpoch), 0))
                return True

    # def cleanOrder(self):
        
    
