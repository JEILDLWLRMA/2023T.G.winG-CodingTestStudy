## 백준 11501번 - 주식

t = int(input())

profit = []

for i in range(t):
    n = int(input())
    stock_list = list(map(int, input().split()))

    ptr = n-1
    max_price = stock_list[ptr]
    result = 0
    while ptr >= 1:
        if max_price < stock_list[ptr-1]:
            max_price = stock_list[ptr-1]
        else:
            result += (max_price-stock_list[ptr-1])
        ptr -= 1
    profit.append(result)

print(*profit, sep="\n")

