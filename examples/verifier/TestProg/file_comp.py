import csv
import time

import filecmp

file_name_1 = "output_seq_1.csv"
file_name_2 = "output_dask_1.csv"
#file_name_2 = "output_seq_1_mod.csv"




outfile1 = "out1.csv"
outfile2 = "out2.csv"




# Read data from file
def readfile(file_name):

    retval = []
    chunksize=1000
    loop=0
    breakpoint =-20

    file = open(file_name)
    reader = csv.reader(file)
    for i, line in enumerate(reader):
   
        if(loop==breakpoint):
            break
        if (i % chunksize == 0 and i > 0):        
            chunk = []

        data = int(line[0])
        retval.append(data)
    
        loop+=1

    file.close() 
    return retval

# Write to file
def writeTofile(filename, output_data_write):
    with open(filename, 'w') as file:
        file.write('\n'.join(str(data) for data in output_data_write))

data1 = readfile(file_name_1)
print("Input 1 read complete")
data1.sort()
print("Sorting data 1 complete")
writeTofile(outfile1, data1)
print("Write file 1 complete")
data1 = []


data2 = readfile(file_name_2)
print("Input 2 read complete")
data2.sort()
print("Sorting data 2 complete")
writeTofile(outfile2, data2)
print("Write file 2 complete")
data2 = []

result = filecmp.cmp(outfile1, outfile2, shallow=False)
print(result)
print("")
print("")

if (result):
    print("Files are identical")
else:
    print("Files are not identical")
    






	
