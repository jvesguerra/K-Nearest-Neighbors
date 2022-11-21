import csv
import math

data = []
test_data = []
distance_list = []
k_neighbors = []
k_index = []

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

for row_in in range(0,1):    # loop to the inputs
    for row_data in range(0,1):         # test the inputs to all of the current data
        # for col_data in range(0,traverse_col):  # to select points
        #     print("CURRENT",data[row_data][col_data], " ", data[row_data][col_data+1])
        #     print("TEST DATA",test_data[row_in][col_data], " ", test_data[row_in][col_data+1])
        #     print(" ")
        print("NEW ROW")
        # check computation
        eudistance = 0
        for col in range(0,(each_row_length-1)):
            
            x = float(test_data[row_in][col])
            v = float(data[row_data][col])
            eudistance = ((x - v)**2) + eudistance
            #eudistance = math.sqrt(eudistance)
            print("x",test_data[row_in][col]," - ", "v",data[row_data][col]," ",x-v)
            print("distace = ", eudistance)
            if(col == (each_row_length-2)):
                eudistance = math.sqrt(eudistance)
                print("distace = ", eudistance)
                distance_list.append(eudistance)
                data[row_data].append(eudistance)
                #print("distace = ", eudistance)
        # check computation

        
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
        new_output = "No Diabetes"
    else:
        new_output = "With Diabetes"

    #print("appending")
    test_data[row_in].append(new_output)


# for i in range(0,input_length):
#     print(test_data[i])
