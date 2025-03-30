import numpy

data = "Bus_Data_Info/bus_services.csv"

data1 = "Bus_Data_Info/bus_stops.csv"

data2 = "Bus_Data_Info/bus_routes.csv"

file = open (data, "r")

file2 = open (data1, "r")

file3 = open (data2, "r")

print(file.read())

file.close()
