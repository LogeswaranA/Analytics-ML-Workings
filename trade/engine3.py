from collections import deque
import heapq
import uuid
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Order():
    def __init__(self,price,quantity,order_type):
        self.order_id = str(uuid.uuid4())
        self.price = price
        self.quantity = quantity
        self.order_type = order_type

    def __lt__(self, other):
        if self.order_type == "buy":
            return self.price > other.price
        else:
            return self.price < other.price
        
    def __repr__(self):
        return f"{self.order_type.capitalize()} Order(id:{self.order_id}, price:{self.price}, quantity:{self.quantity} )"

class OrderBook():
    def __init__(self):
        self.buy_order=[]
        self.sell_order=[]

    def addOrder(self,order):
        if order.order_type=="buy":
            heapq.heappush(self.buy_order,order)
        else:
            heapq.heappush(self.sell_order,order)

    def removeOrder(self,order_id,order_type):
        if order_type=="buy":
            self.buy_order = [order for order in self.buy_order if order.order_id!=order_id]
            heapq.heapify(self.buy_order)
        else:
            self.sell_order = [order for order in self.sell_order if order.order_id!=order_id]
            heapq.heapify(self.sell_order)
    
    def getBestBuy(self):
        return self.buy_order[0] if self.buy_order else None
    
    def getBestSell(self):
        return self.sell_order[0] if self.sell_order else None
    

class TradeEngine():
    
    def __init__(self):
        self.orderBook = OrderBook()
        self.tradeHistory = deque()

    def submitOrder(self,price,quantity,order_type):
        order = Order(price,quantity,order_type)
        self.orderBook.addOrder(order)
        self.matchOrder()
        return order.order_id
    
    def cancelOrder(self,order_id,order_type):
        self.orderBook.removeOrder(order_id,order_type)
    
    def matchOrder(self):
        while self.orderBook.getBestBuy() and self.orderBook.getBestSell():
            bestbuy = self.orderBook.getBestBuy()
            bestsell = self.orderBook.getBestSell()
            if bestbuy.price >= bestsell.price:
                trade_quantity = min(bestbuy.quantity,bestsell.quantity)
                trade_price = bestsell.price

                self.tradeHistory.append((bestsell.order_id,bestbuy.order_id,trade_price,trade_quantity))
                if bestbuy.quantity > bestsell.quantity:
                    bestbuy.quantity -= trade_quantity
                    heapq.heappop(self.orderBook.sell_order)
                elif bestbuy.quantity < bestsell.quantity:
                    bestsell.quantity -= trade_quantity
                    heapq.heappop(self.orderBook.buy_order)
                else:
                    heapq.heappop(self.orderBook.buy_order)
                    heapq.heappop(self.orderBook.sell_order)
            else:
                break

    def getTradeHistory(self):
        return list(self.tradeHistory)


if __name__ == "__main__":

    engine = TradeEngine()
    engine.submitOrder(100, 10, 'buy')
    engine.submitOrder(90, 5, 'sell')
    engine.submitOrder(95, 2, 'buy')
    engine.submitOrder(85, 7, 'sell')

    print(engine.getTradeHistory())
    logger.info("I am here")

    
