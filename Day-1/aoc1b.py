heights = []
total = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

heights = [int(item) for item in lines]

window = []

for i, j, k in zip(heights, heights[1:], heights[2:]):
    window.append(i+j+k)

for x, y in zip(window, window[1:]):
    if y>x:
        total = total + 1

print (total)