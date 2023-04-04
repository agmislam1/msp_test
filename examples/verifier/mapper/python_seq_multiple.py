import csv
import time
import os
import glob

file_name = "input_data_0.csv"
output_file_seq = "output_seq_1.csv"


def writeTofile(filename, output_data_write):
    with open(filename, 'w') as file:
        file.write('\n'.join(str(data) for data in output_data_write))


chunksize=1000





chunk = []
input_data_seq = []







### Read file
def read_files(file_name):
    loop = 0
    breakpoint = -20

    file = open(file_name)
    reader = csv.reader(file)
    for i, line in enumerate(reader):
        
        if(loop==breakpoint):
            break
        if (i % chunksize == 0 and i > 0):
        
            del chunk[:]  # or: chunk = []
        data = int(line[0])
        input_data_seq.append(data)
    
        loop+=1

    file.close() 

    


## Read all the files
start = time.time()
filecount = 0
all_files = glob.glob("input_data_*.csv")
for file in all_files:
    read_files(file)
    filecount = filecount + 1
end = time.time()    

print("Time taken to read " + str(filecount) +" files: " + str(end - start))


      

    
      



def check(val1):   

    val1=val1+1
    return val1*val1

def sum_array(numbers):
    print("Sequential Program Started")
    
    num = 0
    i=0
    
    for val in numbers:
       numbers[i] = check(val)
       i=i+1
       
    return numbers
	


import time

output=[]
start = time.time()
output = sum_array(input_data_seq)
end = time.time()

delta = (end - start)/3600


print("Time taken to execute the code: " + str(end - start))

print(output[:4])
	
