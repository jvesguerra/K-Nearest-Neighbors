import csv
import math

data = []
test_data = []
distance_list = []
k_neighbors = []
k_index = []
class_0 = []
class_1 = []
min_value_arr = []

k = 5

with open("./diabetes.csv",'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)

with open("./input.in",'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        test_data.append(row)
        #print(row)

# for current data
data_length = len(data) 
each_row_length = len(data[0]) #3
class_index = each_row_length -1

# for input data
input_length = len(test_data)
each_input_length = len(test_data[0])

traverse_col = each_row_length - 2

for row_in in range(0,input_length):    # loop to the inputs
    print(test_data[row_in])
    print("")
    for row_data in range(0,data_length):         # test the inputs to all of the current data
        eudistance = 0
        for col in range(0,(each_row_length-1)):
            x = float(test_data[row_in][col])
            v = float(data[row_data][col])
            eudistance = ((x - v)**2) + eudistance
            if(col == (each_row_length-2)):
                eudistance = math.sqrt(eudistance)
                distance_list.append(eudistance)

    # get the location of the min values
    for i in range(0,k):
        min_value = min(distance_list)
        min_index = distance_list.index(min_value)
        k_index.append(min_index)
        distance_list[min_index] = 99999;

        #min_value_arr.append(min_index)

    k_index.sort()

    # append to kneighbors array the nearest values
    for i in range(0,k):
        min_index = k_index[i]
        k_neighbors.append(data[min_index])

        #k_neighbors.append(min_value_arr[i])


    # checking k neighbors only
    for i in range(0,k):
        #print(k_neighbors[i][each_row_length])
        print(k_neighbors[i])
    print(" ")

    for i in range(0,k):
        #output = k_neighbors[i][class_index]
        output = int(k_neighbors[i][class_index])
        if output == 1:
            class_1.append(k_neighbors[i])
        else:
            class_0.append(k_neighbors[i])

    print("Class 0 = ", len(class_0))
    print("Class 1 = ", len(class_1))

    if len(class_0) > len(class_1):
        new_output = "With Diabetes"
    else:
        new_output = "No Diabetes"

    test_data[row_in].append(new_output)

    #reset values
    distance_list.clear()
    k_index.clear()
    k_neighbors.clear()
    class_0.clear()
    class_1.clear()
    eudistance = 0

    min_value_arr.clear()

for i in range(0,input_length):
    print(test_data[i])
