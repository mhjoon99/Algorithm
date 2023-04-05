n = int(input())
way = input().split()

location = [1, 1]

L = [-1, 0]
R = [1, 0]
U = [0, -1]
D = [0, 1]


for i in way:
    match i:
        case 'L':
            if location[0] <= 1:
                continue
            else:
                location = [x + y for x, y in zip(location,L)]
                print(location)
        case 'R':
            if location[0] >= n:
                continue
            else:
                location = [x + y for x, y in zip(location,R)]
                print(location)
        case 'U':
            if location[1] <= 1:
                continue
            else:
                location = [x + y for x, y in zip(location,U)]
                print(location)
        case 'D':
            if location[1] >= n:
                continue
            else:
                location = [x + y for x, y in zip(location,D)]
                print(location)

print(location[0], location[1])