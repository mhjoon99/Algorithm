n, k = map(int, input().split())

result = 0

# N이 1이 될때까지 반복문 실행
while (n != 1):
    if(n % k == 0): # N이 K로 나누어 떨어지면 N/K
        n //= k
        result += 1
    else:   # N이 K로 나누어 떨어지지 않으면 N-1
        n -= 1
        result += 1

print(result)