# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
index = list(map(int, input().split()))

index.sort(reverse=True)    # 입력받은 수 정렬
first = index[0]    # 첫번째로 큰 수
second = index[1]   # 두번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k 번 더하기
        if m == 0:
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second    # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)   #최종 답안 출력