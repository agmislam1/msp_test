import time
def maxNum(numbers):
    max1 = 0
    for n in numbers:
        if n > max1:
            max1 = n
    return max1



def test_case():
    assert maxNum([1,2,3,4]) == 4


ste = time.time()
input = [1,3,6,7,23,6,778,32453,463,73,37,478,23]
print(maxNum(input))
print(time.time() - ste)
