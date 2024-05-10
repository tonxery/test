"""
下面定义变量会被其它变量引用
class BarSeries:
    open: list = []
    high: list = []
    low: list = []
    close: list = []

    def update_bar(self,bar: dict):
        # 更新K线
        self.open.append(bar["open"])
        self.high.append(bar["high"])
        self.low.append(bar["low"])
        self.close.append(bar["close"])

    def print_data(self):
        # 打印数据
        print("开盘价序列",self.open)
        print("最高价序列",self.high)
        print("最低价序列",self.low)
        print("收盘价序列",self.close)
"""


class NewBarSeries:
    def __init__(self):
        self.open: list = []
        self.high: list = []
        self.low: list = []
        self.close: list = []

    def update_bar(self,bar: dict):
        """更新K线"""
        self.open.append(bar["open"])
        self.high.append(bar["high"])
        self.low.append(bar["low"])
        self.close.append(bar["close"])

    def print_data(self):
        """打印数据"""
        print("开盘价序列",self.open)
        print("最高价序列",self.high)
        print("最低价序列",self.low)
        print("收盘价序列",self.close)


if __name__ == "__main__":
    bar = {
        "open": 100,
        "high": 150,
        "low":  99,
        "close": 89,
    }
    """
    bs1 = BarSeries()
    bs1.update_bar(bar)
    bs1.print_data()

    bs2 = BarSeries()
    bs2.update_bar(bar)
    bs2.print_data()
    """
    bs1 = NewBarSeries()
    bs1.update_bar(bar)
    bs1.print_data()

    bs2 = NewBarSeries()
    bs2.update_bar(bar)
    bs2.print_data()