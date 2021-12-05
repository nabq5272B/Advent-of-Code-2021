with open('Day-2/input.txt', 'r') as f:
    lines = f.readlines()

list = [str(item) for item in lines]

forward = aim = depth = 0

for i in list:
    if i[0:7] == 'forward':
        forward = forward + int(i[-2])
        depth = depth + aim*int(i[-2])
    elif i[0:4] == 'down':
        aim = aim + int(i[-2])
    elif i[0:2] == 'up':
        aim = aim - int(i[-2])

result = forward*depth
print(result)
