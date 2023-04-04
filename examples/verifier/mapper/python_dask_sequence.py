import csv
import time

#from distributed import Client
# client = Client()


output_file_dask = "output_dask_1.csv"

file_name = "input_data_0.csv"

def writeTofile(filename, output_data_write):
    with open(filename, 'w') as file:
        file.write('\n'.join(str(data) for data in output_data_write))
		



import dask.bag as daskbag
import dask



number_of_partitions = 500


def check(val1):

    val1=val1+1
    return val1*val1
	
def run_prog():

	
	chunksize=1000

	loop=0
	breakpoint =-100

	file = open(file_name)
	reader = csv.reader(file)

	chunk = []
	input_data_dask = []


	start = time.time()
	for i, line in enumerate(reader):
	   
		if(loop==breakpoint):
			break
		if (i % chunksize == 0 and i > 0):
			
			del chunk[:]  # or: chunk = []
		data = int(line[0])
		input_data_dask.append(data)
		
		loop+=1

	file.close() 

	end = time.time()

	print("Time taken to read the file: " + str(end - start))

	print(input_data_dask[:4])

	output = sum_array(input_data_dask)
	print(output[:4])
	print(len(output))

def sum_array(numbers):
    print("Dask Bag Program Started")
    
    num = 0
    i=0
    start = time.time()
    numbers_bag_0 = daskbag.from_sequence(numbers,npartitions=number_of_partitions)
   
    print("Dask Bag Created")
    start1 = time.time()
    
    print("Time taken to create the bag: " + str(start1 - start))
    
    
    numbers_bag_1 = numbers_bag_0.map(lambda val1: val1+1)
    numbers = numbers_bag_1.map(lambda val1: val1*val1).compute(num_workers=4)
    
    end = time.time()
    
    print("Time taken to execute the code: " + str(end - start1))
       
    return numbers

if __name__ == '__main__':
	run_prog()



