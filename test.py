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

contract_priceticks.update(ic_priceticks) #更新字典
print(contract_priceticks)
