import csv
import time
## For AST analysis for ParallelPy

def count_array(numbers):
    count_all = 0
    i=0
    for n in numbers:
        count_all = count_all + 1
        i+=1
    return count_all


number = []
with open('1.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        row = [ int(i) for i in row]
        number += row
        
ste = time.time()
print(count_array(number))
print(time.time() - ste)

