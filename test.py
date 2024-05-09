symbol = "IO2010-C-2700"
print(symbol)
exchange = "CFFEX"
vt_symbol = f"{symbol}.CFFEX" #格式化字符串
vt_symbol1 = f"{symbol}.{exchange}"
print(vt_symbol1)
print("\"Hello World\"")
a = 100.11
print(f"{a:.0f}")
print(f"{a:.1f}")
print(f"{a:.2f}")
print(f"{a:.3f}")

price = 150.2
volume = 10
directon = "买"
print(f"执行下单{symbol},{directon} {volume}手@{price:.2f}")
#执行下单IO2010-C-2700,买 10手@1

#大小写
b = "hello"
print(b.capitalize()) #首字母大小
print(b.lower()) #所有小写
print(b.upper()) #所有大写

#填充
order_count = 5
orderid = str(order_count).rjust(8,"0")  #生成委托单号,右侧填充,8位长字符串,空的用0填充
print(orderid,type(orderid))

#查找与替换
print(symbol,symbol.index("-C-")) #查找字符串在什么位置
print(symbol.replace("-",""))
print(symbol.replace("-C-","+H+"))  #查找并替换
print(symbol.startswith("IO"))      #查找开始

underlying_symbol,strike_price = symbol.split("-C-")
print(underlying_symbol,strike_price,type(strike_price))
print(type(int(strike_price)))

#类型检查
symbol = "600036"
print(symbol.isdigit())  #检查是否数字
symbol  = "ES"
print(symbol.isalpha())  #检查字符串

symbols = list()  #合约列表
symbols = []      #同上创建列表
symbols = ["IF2009","IF2010","IF2012","IF2103"]
print(type(symbols),symbols[0],symbols[-1],symbols[:]) #正负数下标
ih_symbols = []
ih_symbols.append("IH2009") #添加元素
ih_symbols.append("IH2010")
ih_symbols.insert(1,"IH2022") #指定位置插入
ih_symbols[1] = "IH2033"
ih_symbols.pop()              #移除最后一个值
print(ih_symbols)
for i in ih_symbols:
    print(i)

for i in range(0,len(ih_symbols)):
    print(i,ih_symbols[i])


#字典
a = {}
type(a)
a = dict()
contract_priceticks = {
    "IF2009":0.2,
    "rb2101":1,
    "600036":0.01
}
print(type(contract_priceticks),contract_priceticks)

l = [("IF2009",0.2),("rb2101",1.0),("600036",0.01)]
a = dict(l)
print(a)
print({str(i):i*i for i in range(10)})  #str(i)键,i*i值

pricetick = contract_priceticks["IF2009"]
print(pricetick)
contract_priceticks["IH2010"] = 0.2
print(contract_priceticks)

for symbol in ['IF2009', 'rb2101', '600036', 'IH2010']:
    contract_priceticks[symbol] = 0.2
print(contract_priceticks)

#del contract_priceticks["IC2009"]  #删除字典某个值

#循环遍历
for symbol in contract_priceticks:
    print(symbol)

for pricetick in contract_priceticks:
    print(pricetick)

for symbol,pricetick in contract_priceticks.items():
    print(f"{symbol}合约值价格跳动是,{pricetick}")

print("IC2009" in contract_priceticks) #逻辑判断
print(contract_priceticks.get("IC2009",0)) #查询值,查不到返回0

ic_priceticks = {
    "IF2009": 3.3,
    "rb2101": 1,
    "600036": 5.8
}
#tewst



contract_priceticks.update(ic_priceticks) #更新字典
print(contract_priceticks)

a = set()
print(a)
b = {1,2,3,4,5}
print(b,type(b))
a.add(10)
a.add(8)
a.remove(8)
b.update({6,7,8,9,10})
for i in  b:
    print(i)
print(b)
if 5 in b:
    print("True")
b.clear()
print(b)
if_symblos = {"IF2009","IF2010"}
ih_symbols = {"IH2009","IH2010"}
new_symbols = if_symblos.union(ih_symbols)
print(new_symbols)
print(if_symblos,ih_symbols)
print("---------")
# if_symblos.insersection(ih_symbols)
print(if_symblos.difference(ih_symbols))

a1 = tuple()
b1 = (1,2,3,4,5)
print(b1)
print(b1[0])
# b1[0] = 7
print(b1)
for i in b1:
    print(i)
c1  = (8,)
print(c1)
l = [1,2,3,4,5,6]
e = tuple(l)
print(e)

info_d = {
    "symbol": "IF2009",
    "direction": "Buy",
    "price": 3800,
    "volume": 1
}
symbol = info_d["symbol"]
dirction = info_d["direction"]
price = info_d["price"]
volume = info_d["volume"]

print(f"{symbol}发出委托，  {dirction} {volume}手@{price}")

info_t = ("IF2009","Buy",3800,1)
symbol,directon1,pricel,volume1 = info_t
print(symbol,directon1,pricel,volume1)

symbol2, _, price2, volume2 = info_t
print(symbol2,volume2)

symbol3,  *_, volume3 = info_t
print("---")
print(symbol3,_ , volume3)

bars = []
for i in range(1,5):
    bar = {
        "datatime": f"2020090{i}",
        "open": (100 +i) * 100,
        "high": (100 +i) * 100,
        "low": (100 +i) * 100,
        "close": (100 +i) * 100,
    }
    bars.append(bar)
print(bars)
print("--------------")
for bar in bars:
    print(bar)

last_bar = bars[-1]
print(last_bar)

i = 5
new_bar = {
        "datatime": f"2020090{i}",
        "open": (100 +i) * 100,
        "high": (100 +i) * 100,
        "low": (100 +i) * 100,
        "close": (100 +i) * 100,
    }
bars.pop(0)
bars.append(new_bar)
print("-------------")
for bar in bars:
    print(bar)

active_orderids = {}
strategy_name = "demo_strategy"
active_orderids["strategy_name"] = "strategy_orderids"
print("============")
print(active_orderids)

d = {}
# l = [1,2,3]
# t = (5,5,8)
# d[l[0]] = 1
# print(d)
# s1 = set()
# print(type(s1))
# s1.add(l)
# print(s1)

d[123] = l
tp = (1,2,3)
print(tp)
tp = (1,2,l)
print(tp)