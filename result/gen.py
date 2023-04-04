import dask.bag as daskbag 

from dask.distributed import Client
import json
workers=32
partition=100
blocksize = '256MB'
import csv
import time
## For AST analysis for ParallelPy

def count_array(numbers):
    count_all = 0
    i=0
    count_all_DASK = daskbag.read_text('input.csv',blocksize=blocksize).str.strip()
	count_all_DASK = count_all_DASK.map(lambda x: [int(num) for num in x.split(',')])
	count_all_DASK = count_all_DASK.flatten()
    with Client(n_workers=workers) as client:
		count_all=count_all_DASK.count().compute()
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

