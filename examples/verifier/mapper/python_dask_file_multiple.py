import csv
import time

output_file_dask = "output_dask_1.csv"


def writeTofile(filename, output_data_write):
    with open(filename, 'w') as file:
        file.write('\n'.join(str(data) for data in output_data_write))
		
		
import dask.bag as daskbag
import json



output = []
blocksize = '1MB'

def check(val1):

    val1=val1+1
    return val1*val1

def sum_array():
    print("Dask Bag Program Started")
    
    num = 0
    i=0
    start = time.time()

    
    numbers_bag_0 = daskbag.read_text('input_data_*.csv',blocksize=blocksize).map(json.loads)
    
   
    start1 = time.time()
    print("Time taken to create the bag: " + str(start1 - start))
    numbers_bag_1 = numbers_bag_0.map(lambda val1: val1+1)
    numbers = numbers_bag_1.map(lambda val1: val1*val1).compute(scheduler='processes',num_workers=4)
       
    end = time.time()
    

    print("Time taken to execute the code: " + str(end - start1))
    
    
    
    #bag = numbers_bag_0.map(lambda val1: val1+1).map(lambda val1: val1*val1)
    #numbers = bag.compute()
       
    return numbers
	
	
def run_prog():
	output = sum_array()
	print(output[:6])
	print(len(output))
	
if __name__ == '__main__':
	run_prog()