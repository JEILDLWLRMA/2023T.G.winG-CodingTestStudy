## 실전 문제 왕실의 나이트

point = input()

keyword = {'UL':[-2, -1],                 # Definition of Keyword
           'UR':[-2, +1],                 # 'Move Twice Move Once' : [ Move In Col, Move in Row]
           'DL':[+2, -1],
           'DR':[+2, +1],
           'LU':[+1, -2],
           'LD':[+1, +2],
           'RU':[-1, +2],
           'RD':[+1, -2]}

point = [point[0], int(point[1])]       # Initialize Point
count = 0                               # Initialize Count

for move in keyword:             
    temp = [chr(ord(point[0]) + keyword.get(move)[0]), point[1] + keyword.get(move)[1]]
    if(temp[0]>'h' or temp[0]<'a' or temp[1]>8 or temp[1]<1):
        pass
    else:
        count+=1

print(count)