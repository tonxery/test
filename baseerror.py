"""
def demo1():
    a = 1
    b = 2
    c = a + b
    return c

def demo2():
    symbol_exchange_map = {
        "IF2010": "CFFEX",
        "rb2101": "SHFE",
        "m2101": "DCE",
        "SR101": "CZCE",
    }

    exchange = symbol_exchange_map["rb2101"]
    # exchange = symbol_exchange_map["IC2101"]
    return exchange

i = 0
def demo3():
    global i
    i += 1
    print(f"调用Demo3函数，第{i}次")
    demo3()


def add(a,b):
    return  a + b

def test():
    n = 1
    for i in [1,2.0,-3,True,"test"]:
        try:
            m = add(i,n)
            print(m)
        #预测错误位置
        except TypeError:
            print("调用add函数出错，错误数据",i)
        finally:
            print(f"{i}数据调用add计算结束")

def main():
    print("开始运行测试")
    test()

main()
"""

#求和
def sum_even(n):
    result = 0
    for i in range(0,n,2):
        # print(i)
        # assert(i % 2 == 0)  #断言，为True偶数正常，非０异常
        result += i
    return result

n = sum_even(50)
print(n)

from datetime import datetime
print("当前时间是：",datetime.now())