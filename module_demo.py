from datetime import date,time,datetime,timedelta
print(f"当前片段代码运行所在的命名空间是{__name__}")

#求自增和
def sum_even(n):
    result = 0
    for i in range(0,n,2):
        # print(i)
        # assert(i % 2 == 0)  #断言，为True偶数正常，非０异常
        result += i
    return result

if __name__ == "__main__":
    n = sum_even(50)
    print("sum_even函数测试结果为",n)

    current_dt = datetime.now()

    end_time = time(14,55)
    current_time = current_dt.time()
    if current_time >= end_time:
        print("该执行平仓操作")
    else:
        print("执行正常交易操作")

    option_expiry = datetime(2020,10,28)
    current_dt = datetime.now()
    time_left = option_expiry - current_dt
    print(time_left,type(time_left))
    print("剩余天数",time_left.days)
    print("剩余秒数",time_left.total_seconds())
    #datetime转字符串
    print(current_dt.strftime("%Y-%m-%d %H:%M:%S"))
    #字符串转datetime
    demo_str = "2020/9/27 204635"
    demo_dt = datetime.strptime(demo_str,"%Y/%m/%d %H%M%S")
    print(demo_dt,type(demo_dt))

import torch
torch.onnx.export(model)
