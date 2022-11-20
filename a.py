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
with open("./sample.csv",'r',encoding='utf-8') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)
        #print(row)

each_row_length = len(data[0]) #3
data_length = len(data) #12

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
    print(min_value)
    min_index = distance_list.index(min_value)
    k_index.append(min_index)
    distance_list[min_index] = 9999;

k_index.sort()

for i in range(0,k):
    min_index = k_index[i]
    k_neighbors.append(data[min_index])





    



