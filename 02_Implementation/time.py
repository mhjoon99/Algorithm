n = int(input())

count = 0

for hour in range(n+1):
    for min in range(60):
        for sec in range(60):
            time = str(hour)+str(min)+str(sec)
            if '3' in time:
                count+=1

print(count)
