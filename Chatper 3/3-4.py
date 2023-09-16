## 실전 문제 1이 될 때까지

n, k = map(int, input().split())

count = 0
while n>=k:
    if(n%k==0):
        count += 1
        n//=k
    else:
        count += 1
        n -= 1

count += (n-1)
print(count)