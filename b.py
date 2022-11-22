import csv
import math

data = []
test_data = []
distance_list = []
k_neighbors = []
k_index = []
class_0 = []
class_1 = []
class_2 = []
class_3 = []
class_4 = []
classes = []
classes.append(class_0)
classes.append(class_1)
classes.append(class_2)
classes.append(class_3)
classes.append(class_4)
classes_count = []
min_value_arr = []

#k = 5
k = int(input("Enter k: "))

f = open("output.txt","w")

with open("./fruits.csv",'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)

with open("./in.in",'r') as file:
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

for row_in in range(0,input_length):    # loop to the inputs
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

    for i in range(0,k):
        #output = k_neighbors[i][class_index]
        output = int(k_neighbors[i][class_index])
        if output == 1:
            classes[1].append(k_neighbors[i])
        elif output == 2:
            classes[2].append(k_neighbors[i])
        elif output == 3:
            classes[3].append(k_neighbors[i])
        elif output == 4:
            classes[4].append(k_neighbors[i])
        else:
            classes[0].append(k_neighbors[i])

    # get max value
    for i in range(0,5): # 5 number of classes
        classes_count.append(len(classes[i]))

    max_value = max(classes_count)
    max_index = classes_count.index(max_value)
    
    new_output = max_index

    # if new_output == 1:
    #     new_output = "With Diabetes"
    # else:
    #     new_output = "No Diabetes"

    test_data[row_in].append(new_output)
    
    #reset values
    distance_list.clear()
    k_index.clear()
    k_neighbors.clear()
    eudistance = 0
    classes_count.clear()

    for i in range(0,5):
        classes[i].clear()

    min_value_arr.clear()

#write to out

with open('fruits-out.csv','w',newline='') as file:
    writer = csv.writer(file)
    for i in range(0,data_length):
        writer.writerow(data[i])
    for i in range(0,input_length):
        writer.writerow(test_data[i])

# with open('diabetes-out.csv','w',newline='') as file:
#     writer = csv.writer(file)
#     for i in range(0,data_length):
#         writer.writerow(data[i])
#     for i in range(0,input_length):
#         writer.writerow(test_data[i])

for line in test_data:
    f.write("%s "%line)
    f.write("\n")

print("Done! Check output.txt")
