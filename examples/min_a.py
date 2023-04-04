import time

def minNum(numbers):
    min1 = 999999
    for n in numbers:
        if n < min1:
            min1 = n
    return min1



def test_case():
    assert minNum([1,2,3,4]) == 1


ste = time.time()
input = [1,3,6,7,23,6,778,32453,463,73,37,478,23]
print(minNum(input))
print(time.time() - ste)