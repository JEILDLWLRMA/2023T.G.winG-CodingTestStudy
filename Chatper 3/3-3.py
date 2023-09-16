## 실전 문제 숫자 카드 게임

n, m = map(int, input().split())
result = 0
for i in range(n):
    input_list = list(map(int, input().split()))
    input_list.sort()
    if(input_list[0]>=result):result=input_list[0]

print(result)
