n = input()

# length = 입력받은 숫자 길이
length = len(n)
str = []

# n에서 입력받은 숫자 각 원소가 숫자인 list로 str에 저장
for i in range(length):
    str = list(map(int,n))

# head = 왼쪽 부분 / rear = 오른쪽 부분
head=0
rear=0

# head에 왼쪽 부분 각 숫자 합 저장 / rear에 오른쪽 부분 각 숫자 합 저장
for i in range(length):
    if i < length/2:
        head += str[i]
    else:
        rear += str[i]

# 왼쪽 부분과 오른쪽 부분 일치: LUCKY / 불일치: READY 출력
if head == rear:
    print("LUCKY")
else:
    print("READY")