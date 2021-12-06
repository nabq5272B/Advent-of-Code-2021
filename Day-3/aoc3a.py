with open('Day-3/input.txt', 'r') as f:
    lines = f.readlines()

list = [str(item) for item in lines]

def binary(given_list, term):
    zero = 0
    one = 0
    for i in given_list:
        for j in range(0, len(given_list)):
            if j == term:
                if i[j] == '0':
                    zero = zero + 1
                elif i[j] == '1':
                    one = one + 1

    return zero, one

gamma = []

for i  in range(0, len(list)):

    print(binary(list, i))