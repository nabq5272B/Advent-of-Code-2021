with open('input.txt', 'r') as f:
    lines = f.readlines()

forward_list = []
down_list = []
up_list = []

list =  [str(item) for item in lines]

for i in list:
    if i[0:7] == 'forward':
        forward_list.append(i[-2])

    elif i[0:4] == 'down':
        down_list.append(i[-2])

    elif i[0:2] == 'up':
        up_list.append(i[-2])

forward_list.remove(' ')

forward_list = [int(i) for i in forward_list]
down_list = [int(i) for i in down_list]
up_list = [int(i) for i in up_list]

forward_list.append(7)

forward = sum(forward_list) 
down = sum(down_list)
up = sum(up_list)

result = forward * (down - up)

print(result)