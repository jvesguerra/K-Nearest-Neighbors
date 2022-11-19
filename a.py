import csv
import math

# file.csv data
# data[n] is the first line in the csv
# data[0][n] is to access the data inside each row
data = []   
k = 4
distace_list = []

# open csv file then save data in rows to data array
with open("./sample.csv",'r',encoding='utf-8') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)
        print(row)

each_row_length = len(data[0]) #3
data_length = len(data) #12

# each_row_length - 1 = output/ outcome/ class
for row in range(0,data_length):
    eudistance = 0
    for col in range(0,(each_row_length-1)):
        num = float(data[row][col])
        eudistance = ((num - k)**2) + eudistance
        if(col == (each_row_length-2)):
            eudistance = math.sqrt(eudistance)
            distace_list.append(eudistance)

print(distace_list)

