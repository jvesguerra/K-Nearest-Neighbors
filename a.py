import csv
import math

# file.csv data
# data[n] is the first line in the csv
# data[0][n] is to access the data inside each row
data = []   
input_data = [[4,4]]
distance_list = []
k_neighbors = []
k_index = []

k = 5
k_counter = 0

# open csv file then save data in rows to data array
with open("./sample.csv",'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)
        #print(row)

each_row_length = len(data[0]) #3
class_index = each_row_length -1
data_length = len(data) #12

#for run in range(0,len(input_data)):
# compute for euclidean distance
for input_row in range(0,len(input_data)):
    # each_row_length - 1 = output/ outcome/ class
    for row in range(0,data_length):
        eudistance = 0
        for col in range(0,(each_row_length-1)):
            x = input_data[input_row][col]
            v = float(data[row][col])
            eudistance = ((x - v)**2) + eudistance
            if(col == (each_row_length-2)):
                eudistance = math.sqrt(eudistance)
                distance_list.append(eudistance)
                data[row].append(eudistance)


# get the location of the min values
for i in range(0,k):
    min_value = min(distance_list)
    min_index = distance_list.index(min_value)
    k_index.append(min_index)
    distance_list[min_index] = 9999;

k_index.sort()

# append to kneighbors array the nearest values
for i in range(0,k):
    min_index = k_index[i]
    k_neighbors.append(data[min_index])

count_of_0 = 0
count_of_1 = 0

for i in range(0,k):
    output = int(k_neighbors[i][class_index])
    if output == 1:
        count_of_1 += 1
    else:
        count_of_0 += 1


if count_of_0 > count_of_1:
    new_output = 0
else:
    new_output = 1

input0_length = len(input_data[0]) #2

#input_data[run].append(new_output)
input_data[0].append(new_output)

#reset values
distance_list.clear()
k_index.clear()
k_neighbors.clear()

print(input_data)