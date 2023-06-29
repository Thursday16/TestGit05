

'''def sum1(num):
    sum = 0
    for x in range(1, num+1):
        sum += x
    return sum'''

def sum2(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num+sum2(num-1)

def run():
    print(sum2(2))

