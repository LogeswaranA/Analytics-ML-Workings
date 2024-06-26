import uuid
import heapq
from collections import deque

class Order():
    def __init__(self, price, order_type, quantity):
        self.order_id = str(uuid.uuid4())
        self.price = price
        self.order_type = order_type
        self.quantity = quantity

    def __lt__(self,other):
        if self.order_type == "buy":
            return self.price > other.price
        else:
            return self.price < other.price
        
    def __repr__(self):
        return f"{self.order_type.capitalize()} Order(id: {self.order_id}, price: {self.price}, quantity:{self.quantity})"
    
class OrderBook():
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def addOrder(self,order):
        if order.order_type == "buy":
            heapq.heappush(self.buy_orders,order)
        else:
            heapq.heappush(self.sell_orders,order)
    
    def removeOrder(self,order_id,orderType):
        if orderType == "buy":
            self.buy_orders = [order for order in self.buy_orders if order.order_id != order_id]
            heapq.heapify(self.buy_orders)
        else:
            self.sell_orders = [order for order in self.sell_orders if order.order_id != order_id]
            heapq.heapify(self.sell_orders)

    def get_best_buy(self):
        return self.buy_orders[0] if self.buy_orders else None
    

    def get_best_sell(self):
        return self.sell_orders[0] if self.sell_orders else None
    

class TradeEngine():

    def __init__(self):
        self.order_book = OrderBook()
        self.trade_history = deque()

    def submit_order(self,price,quantity,order_type):
        order = Order(price,order_type,quantity)
        self.order_book.addOrder(order)
        self.match_orders()
        return order.order_id
    
    def cancel_order(self,order_id, order_type):
        return self.order_book.removeOrder(order_id,order_type)
    
    def match_orders(self):
        while self.order_book.get_best_sell() and self.order_book.get_best_buy():

            best_buy = self.order_book.get_best_buy()
            best_sell = self.order_book.get_best_sell()

            if best_buy.price >= best_sell.price:
                trade_price = best_sell.price
                trade_quantity = min(best_buy.quantity,best_sell.quantity)

                self.trade_history.append((best_buy.order_id, best_sell.order_id, trade_price, trade_quantity))

                if best_buy.quantity > best_sell.quantity:
                    best_buy.quantity -= trade_quantity
                    heapq.heappop(self.order_book.sell_orders)
                elif best_buy.quantity < best_sell.quantity:
                    best_sell.quantity -= trade_quantity
                    heapq.heappop(self.order_book.buy_orders)
                else:
                    heapq.heappop(self.order_book.buy_orders)
                    heapq.heappop(self.order_book.sell_orders)
            else:
                break

    def get_trade_history(self):
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


