'''
배열을 입력받아 낼 수 있는 최대 이윤 금액을 구하시오
[7,1,2,8,4,1,1,3]
=> 4
[7,44,1,0,11,1,1,3]
'''

import time

def max_profit(stock_arr : list) -> int:
    # profit = []
    min_vl = stock_arr[0]
    max_vl = 0
    for stock in stock_arr:
        min_vl = min(min_vl, stock)
        # profit.append(stock - min_vl)
        max_vl = max(max_vl, stock - min_vl)
    return max_vl
    # return max(profit)
    

if __name__ == '__main__':
    start = time.time()
    print(max_profit([7,44,1,0,11,1,1,3]))
    proc_time = time.time() - start
    print(proc_time)