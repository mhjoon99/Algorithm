# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
index = list(map(int, input().split()))

index.sort(reverse=True)    # 입력받은 수 정렬
first = index[0]    # 첫번째로 큰 수
second = index[1]   # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k      # M이 K+1로 나누어 떨어질 때
count += m % (k+1)                  # M이 K+1로 나누어 떨어지지 않을 때

result = 0
result += (count) * first   # 가장 큰 수 더하기
result += (m - count) * second  # 두번째로 큰 수 더하기

print(result)   #최종 답안 출력