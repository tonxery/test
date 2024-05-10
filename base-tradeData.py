#成交信息
class TradeData:
    def __init__(self):
        self.symbol = ""
        self.datatime = ""
        self.direction = ""
        self.price = 0.0
        self.volume = 0.0

    def calculate_trading_value(self,size):
        #计算成交金额的对象方法
        value = self.price * self.volume * size
        return value

    def to_str(self):
        text = f"{self.datetime}: {self.direction} {self.symbol} {self.volume} 手 @ {self.price}"
        return  text

    #加入如下方法后不会返回对象__main__.TradeData object，
    def __str__(self):
        return self.to_str()

if __name__ == "__main__":
    trade = TradeData()
    trade.symbol = "IF2010"
    trade.datetime = "20200915 13:15:03"
    trade.direction = "买入"
    trade.price = 4200
    trade.symbol = 1
    # print(trade.to_str())
    print(trade)