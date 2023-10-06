## 예제 4-1 상하좌우

n = int(input())
input_list = list(map(str, input().split()))

location = [1, 1]
keyword = {'R':[0, +1], 
           'L':[0, -1,],
           'U':[-1, 0],
           'D': [+1, 0]
           }

for key in input_list:
    temp = [x+y for x, y in zip(location, keyword[key])]
    if 0 in temp:
        pass
    else:
        location = temp

print(*location, sep=" ") 