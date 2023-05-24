import os
import sys
import re
import time
from pyshacl import validate
from rdflib import Graph, Dataset


print("Load shape graph" , end="\t")
##### Create and load the shape graph #####
time_start = time.perf_counter()
shape_graph = Graph()
shape_graph.parse("shacl/shacl-singleton.ttl")
time_end = time.perf_counter()
m, s  = divmod(time_end-time_start,60)
if m > 0:
    print('%sm%ss'%(int(m),s))
else: 
    print('%ss'%(s))


##### Creates the Dataset that will contain the data #####
data_graph = Dataset()
context_graph = data_graph.graph("context")  # Authors


# Loads all Authors to the context graph
print('Load Authors', end='\t\t')
time_start = time.perf_counter()
context_graph = data_graph.graph("context")  
for file in os.listdir("rdf/Authors"):
    context_graph.parse("rdf/Authors/"+file)
time_end = time.perf_counter()
m, s  = divmod(time_end-time_start,60)
if m > 0:
    print('%sm%ss'%(int(m),s))
else: 
    print('%ss'%(s))


##### Find the ER file and arrange them in order #####
ER_dir = "rdf/ER-singleton"
file_list = []
for file in os.listdir(ER_dir):
    if os.path.splitext(file)[1] == '.nt':
        file_list.append(os.path.join(ER_dir, file))
file_list.sort(key=lambda x: int(re.search(r"\d+", x)[0]))

print("\nLoading ERs file by file in the dataset, validating them along the authors.")
##### Load the ER file one by one and validate them one by one, prints the results and times #####
for ER_file in file_list:
    name = ER_file.split('/')[-1]
    num = int(re.search(r"\d+", name)[0])
    print("ER_%s"%num)

    # Loads the ER file
    print("\tLoading ER_%s\t"%num, end="")
    ER = data_graph.graph(name)
    time_start = time.perf_counter()
    ER.parse(ER_file)
    time_end = time.perf_counter()
    m, s  = divmod(time_end-time_start,60)
    if m > 0:
        print('%sm%ss'%(int(m),s), end="")
    else: 
        print('%ss'%(s), end="")
    print("\tdataset size with ER_%s: "%num, len(data_graph))

    # Validate it along the context_graph
    print("\tValidating\t", end="")
    time_start = time.perf_counter()
    results = validate(
        data_graph,
        shacl_graph=shape_graph,
        allow_infos=True,
        allow_warnings=False
    )
    time_end = time.perf_counter()
    m, s  = divmod(time_end-time_start,60)
    if m > 0:
        print('%sm%ss'%(int(m),s), end="")
    else: 
        print('%ss'%(s), end="")
    
    # Print results
    if results[0]:
        print("\tER_%s is valid."%num)
    else:
        print("\tER_%s isn't valid."%num)
    print("\tSaving report\t", end="")
    time_start = time.perf_counter()
    with open("shacl_report_%s-singleton.txt"%num, "w") as f:
        print(results[2], file=f)
    time_end = time.perf_counter()
    m, s  = divmod(time_end-time_start,60)
    if m > 0:
        print('%sm%ss'%(int(m),s))
    else: 
        print('%ss'%(s))
    del results

    # Remove the ER graph from the Dataset in order to load the next ER file
    print("\tRemoving ER_%s\t"%num, end="")
    time_start = time.perf_counter()
    data_graph.remove_graph(ER)
    del ER
    time_end = time.perf_counter()
    m, s  = divmod(time_end-time_start,60)
    if m > 0:
        print('%sm%ss'%(int(m),s), end="")
    else: 
        print('%ss'%(s), end="")
    print("\tdataset size: ", len(data_graph))
