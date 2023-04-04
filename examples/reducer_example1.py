

def multiply(num, a):
    return num * a


def squareacc(numbers):
    num = 1
    
    for i in numbers:
        num = multiply(num, i)
    return num

numbers = [1, 52, 3, 4, 6, 5, 10]
print(squareacc(numbers))


# re = final.map(lambda x: (1, (x[0], x[1]))).reduceByKey(lambda x, y: (((x[0] * y[1]) + y[0]) / (y[1] + 1), 0))