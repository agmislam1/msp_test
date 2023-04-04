
def check(val1):

    val1=val1+1
    return val1*val1

def sum_array(numbers):
    num = 0
    i=0
    
    for val in numbers:
       numbers[i] = check(val)
       i=i+1
       
    return numbers

def test_1():
    expected = [6,7,8]
    
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