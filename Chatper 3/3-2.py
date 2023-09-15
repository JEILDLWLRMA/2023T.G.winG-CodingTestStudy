## 실전 문제 큰 수의 법칙

n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort(reverse=True)

times = m//(k+1)
remain = m%(k+1)

result = (num_list[0] * k + num_list[1]) * times + num_list[0] * remain
print(result)



