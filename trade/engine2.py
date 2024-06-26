import heapq
from collections import deque
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Order():
    def __init__(self,price, quantity, order_type):
        self.order_id = str(uuid.uuid4())
        self.price = price
        self.quantity = quantity
        self.order_type = order_type

    def __lt__(self,other):
        if self.order_type == "buy":
            return self.price > other.price
        else:
            return self.price < other.price
        
    def __repr__(self):
        return f"{self.order_type.capitalize()} Order(id: {self.order_id}, quantity:{self.quantity}, price: {self.price})"
    
class OrderBook():

    def __init__(self):
        self.buy_orders =[]
        self.sell_orders =[]

    def addOrder(self,order):
        if order.order_type == "buy":
            heapq.heappush(self.buy_orders, order)
            logger.info(f"Added buy order: {order.order_id} at {order.price} for {order.quantity}")
        else:
            heapq.heappush(self.sell_orders,order)
            logger.info(f"Added Sell order: {order.order_id} at {order.price} for {order.quantity}")


    def removeOrder(self,order_id,order_type):
        if order_type=="buy":
            self.buy_orders = [order for order in self.buy_orders if order.order_id != order_id]
            heapq.heapify(self.buy_orders)
            logger.info(f"Removed {order_type} order: {order_id}")
        else:
            self.sell_orders = [order for order in self.sell_orders if order.order_id !=order_id]
            heapq.heapify(self.sell_orders)
            logger.info(f"Removed {order_type} order: {order_id}")
    
    def get_best_buy(self):
        return self.buy_orders[0] if self.buy_orders else None
    
    def get_best_sell(self):
        return self.sell_orders[0] if self.sell_orders else None
    

class TradeEngine():

    def __init__(self):
        self.order_book = OrderBook()
        self.trade_history = deque()
    
    def submit_order(self, price, quantity, order_type): 
        order = Order(price,quantity,order_type)
        self.order_book.addOrder(order)
        self.match_order()
        logger.info(f"Submitted {order_type} order: {order.order_id} at {price} for {quantity}")
        return order.order_id
    
    def cancel_order(self,order_id,order_type):
        return self.order_book.removeOrder(order_id,order_type)

    def match_order(self):
        while self.order_book.get_best_buy() and self.order_book.get_best_sell():
            bestbuy = self.order_book.get_best_buy()
            bestsell = self.order_book.get_best_sell()
            print(bestbuy)
            print(bestsell)
            if bestbuy.price >= bestsell.price:
                trade_price = bestbuy.price
                trade_quantity = min(bestbuy.quantity,bestsell.quantity)
                self.trade_history.append((bestbuy.order_id, bestsell.order_id, trade_price, trade_quantity))
                logger.info(f"Matched orders: {bestbuy.order_id} (buy) and {bestsell.order_id} (sell) at {trade_price} for {trade_quantity}")
                if bestbuy.quantity > bestsell.quantity:
                    bestbuy.quantity -= trade_quantity
                    heapq.heappop(self.order_book.sell_orders)
                elif bestbuy.quantity < bestsell.quantity:
                    bestsell.quantity -= trade_quantity
                    heapq.heappop(self.order_book.buy_orders)
                else:
                    heapq.heappop(self.order_book.sell_orders)
                    heapq.heappop(self.order_book.buy_orders)
            else:
                break

    def get_trade_history(self):
        logger.info(f"Retrieved trade history with {len(self.trade_history)} entries")
        return list(self.trade_history)
    

if __name__ == "__main__":
    engine = TradeEngine()

    engine.submit_order(100, 10, 'buy')
    engine.submit_order(90, 5, 'sell')
    engine.submit_order(95, 2, 'buy')
    engine.submit_order(85, 7, 'sell')

        # Display the trade history
    print(engine.get_trade_history())
    
    # Cancel an order
    engine.cancel_order(engine.submit_order(110, 5, 'buy'), 'buy')

    # Submit another order
    engine.submit_order(95, 10, 'sell')

    # Display the trade history again
    print(engine.get_trade_history())









