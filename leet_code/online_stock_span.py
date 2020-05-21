# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3334/


######### My solution. Just works but it is not the best solution. The best solution is using stack #########
class StockSpanner:

    def __init__(self):
        self.price = []
        self.stock_span = []

    def next(self, price: int) -> int:
        if len(self.price) == 0:
            self.price.append(price)
            self.stock_span.append(1)
            
            return 1
        
        if price < self.price[-1]:
            self.stock_span.append(1)
        elif price == self.price[-1]:
            self.stock_span.append((self.stock_span[-1] + 1))
        else:
            prev_index = len(self.price)-1
            curr = self.price[prev_index]
            count = 0
            while curr <= price and prev_index >= 0:
                # print(curr)
                count += self.stock_span[prev_index]
                prev_index = prev_index - self.stock_span[prev_index]
                curr = self.price[prev_index]
            self.stock_span.append(count+1)
        
        self.price.append(price)
        # print('----------------', self.stock_span)
        return self.stock_span[-1]


        
            
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)