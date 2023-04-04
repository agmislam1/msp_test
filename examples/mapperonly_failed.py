
def check(val1, val2):

    val1=val1+val2
    val2 = val1*val2
    return val1+val2

def sum_array(numbers):
    num = 0
    i=0
    val2 = 5
    for val in numbers:
       numbers[i] = check(val,val2)
       i=i+1
       
    return numbers

def test_1():
    expected = [36, 42, 48]
    
    result = sum_array([1,2,3])
    print(result)
    assert result == expected
def test_wrong():
    expected = 8
    result = sum_array([1,2,3,4])
    assert result != expected
def test_2():
    expected = -45
    result = sum_array([10,-50,2,3,-10,7,8,-15])
    assert result == expected


 # re = final.map(lambda x: (1,(x[0],x[1]))).reduceByKey(lambda x,y :  (((x[0] * y[1])+y[0])/(y[1]+1), 0))