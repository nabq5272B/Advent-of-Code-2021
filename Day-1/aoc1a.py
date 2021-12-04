heights = []
total = 0  

with open('input.txt', 'r') as f:
    lines = f.readlines()

heights = [int(item) for item in lines]

for x, y in zip(heights, heights[1:]):
    if y>x:
        total = total + 1

print (total)