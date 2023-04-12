s = list(input())
length = len(s)

alphabet = []
num = 0

# 아스키코드값이 65와 90 사이(대문자값)이면 alphabet 리스트에 입력값을 넣은 후, sort하여 오른차순 정렬
# 그 외의 값(숫자)은 모두 더함
for i in range(length):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        alphabet.append(s[i])
        alphabet.sort()
    else:
        num += int(s[i])

print(''.join(alphabet) + str(num))