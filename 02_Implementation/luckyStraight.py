n = input()

length = int(len(n))
str = []

for i in range(length):
    str = list(map(int,n))

head=0
rear=0

for i in range(length):
    if i < length/2:
        head += str[i]
    else:
        rear += str[i]

if head == rear:
    print("LUCKY")
else:
    print("READY")